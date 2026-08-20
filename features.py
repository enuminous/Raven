import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

EPS = 1e-8

def fit_linear_residuals(df, signal_columns, train_end):
    x = df[signal_columns].astype(float).ffill().fillna(0.0)
    residuals = pd.DataFrame(index=df.index)

    # Each signal is predicted from the other signals; residual becomes the object.
    for target in signal_columns:
        others = [c for c in signal_columns if c != target]
        if not others:
            residuals[f"{target}__resid"] = 0.0
            continue
        model = LinearRegression()
        model.fit(x.loc[:train_end-1, others], x.loc[:train_end-1, target])
        pred = model.predict(x[others])
        residuals[f"{target}__resid"] = x[target].to_numpy() - pred

    return residuals

def build_raven_features(df, signal_columns, train_end, horizons=(3,7,23), random_state=23):
    residuals = fit_linear_residuals(df, signal_columns, train_end)
    out = pd.DataFrame(index=df.index)

    resid_cols = list(residuals.columns)
    for c in resid_cols:
        out[c] = residuals[c]
        out[f"{c}__abs"] = residuals[c].abs()
        out[f"{c}__dx"] = residuals[c].diff().fillna(0.0)

    out["residual_mean_abs"] = residuals.abs().mean(axis=1)
    out["residual_variance"] = residuals.var(axis=1).fillna(0.0)

    # Recurrence proxy: similarity to recent residual magnitude.
    for h in horizons:
        recent = out["residual_mean_abs"].rolling(h, min_periods=1).mean()
        out[f"residual_mean_{h}"] = recent
        out[f"residual_var_{h}"] = out["residual_variance"].rolling(h, min_periods=1).mean()
        out[f"residual_velocity_{h}"] = out["residual_mean_abs"].diff().rolling(h, min_periods=1).mean()

    # Cross-residual coupling.
    coupling = []
    for i,a in enumerate(resid_cols):
        for b in resid_cols[i+1:]:
            corr = residuals[a].rolling(max(horizons), min_periods=5).corr(residuals[b]).fillna(0.0)
            name = f"coupling__{a}__{b}"
            out[name] = corr
            coupling.append(name)

    if coupling:
        out["residual_coupling"] = out[coupling].abs().mean(axis=1)
    else:
        out["residual_coupling"] = 0.0

    # Autocorrelation / persistence.
    autocorrs = []
    for c in resid_cols:
        ac = residuals[c].rolling(max(horizons), min_periods=5).corr(residuals[c].shift(1)).fillna(0.0)
        name = f"{c}__autocorr1"
        out[name] = ac
        autocorrs.append(name)

    out["residual_persistence"] = out[autocorrs].abs().mean(axis=1) if autocorrs else 0.0

    components = [
        out["residual_mean_abs"],
        out["residual_variance"],
        out["residual_coupling"],
        out["residual_persistence"],
    ]
    for h in horizons:
        components.extend([
            out[f"residual_mean_{h}"],
            out[f"residual_var_{h}"],
            out[f"residual_velocity_{h}"].abs(),
        ])

    ranked = pd.concat(components, axis=1).rank(pct=True)
    out["raven_residual_score"] = ranked.mean(axis=1).fillna(0.0)

    # Shuffled-residual control, frozen seed.
    rng = np.random.default_rng(random_state)
    shuffled = residuals.copy()
    for c in shuffled.columns:
        shuffled[c] = rng.permutation(shuffled[c].to_numpy())
    out["shuffled_residual_mean_abs"] = shuffled.abs().mean(axis=1)

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0), residuals
