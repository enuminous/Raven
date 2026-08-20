from dataclasses import dataclass
import pandas as pd

from features import build_raven_features
from baselines import LogisticModel, BaseRateModel, autoregressive_features
from metrics import binary_metrics, residual_summary

@dataclass
class RAVENExperiment:
    time_column: str
    target_column: str
    signal_columns: list
    horizons: tuple = (3,7,23)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, df):
        df = df.sort_values(self.time_column).reset_index(drop=True).copy()
        cut = max(20, int(len(df)*self.train_fraction))
        y = df[self.target_column].astype(int).to_numpy()

        rf, residuals = build_raven_features(
            df,
            self.signal_columns,
            train_end=cut,
            horizons=self.horizons,
            random_state=self.random_state
        )

        raw = df[self.signal_columns].astype(float).ffill().fillna(0.0)
        ar = autoregressive_features(df, self.signal_columns)

        raven_X = pd.concat([raw, rf.drop(columns=["shuffled_residual_mean_abs"])], axis=1).fillna(0.0)
        shuffled_X = pd.concat([
            raw,
            rf[["shuffled_residual_mean_abs"]]
        ], axis=1).fillna(0.0)

        models = {
            "raven": (LogisticModel(self.random_state), raven_X),
            "raw_state": (LogisticModel(self.random_state), raw),
            "autoregressive": (LogisticModel(self.random_state), ar),
            "shuffled_residual": (LogisticModel(self.random_state), shuffled_X),
            "base_rate": (BaseRateModel(), raw),
        }

        results = {}
        for name, (model, X) in models.items():
            model.fit(X.iloc[:cut], y[:cut])
            p = model.predict_proba(X.iloc[cut:])
            results[name] = binary_metrics(y[cut:], p)

        return {
            "n_total": len(df),
            "train_n": cut,
            "test_n": len(df)-cut,
            "residual_summary": residual_summary(residuals.iloc[cut:]),
            "results": results,
            "primary_delta_brier_raw_minus_raven": (
                results["raw_state"]["brier"] - results["raven"]["brier"]
            ),
            "shuffle_delta_brier": (
                results["shuffled_residual"]["brier"] - results["raven"]["brier"]
            ),
            "interpretation": (
                "Positive raw-minus-RAVEN delta favors residual features beyond raw state. "
                "Positive shuffled-minus-RAVEN delta indicates temporal residual structure "
                "performed better than its shuffled control."
            )
        }
