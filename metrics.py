import numpy as np
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score, average_precision_score, accuracy_score

def binary_metrics(y, p):
    y = np.asarray(y, dtype=int)
    p = np.clip(np.asarray(p, dtype=float), 1e-9, 1-1e-9)
    out = {
        "brier": float(brier_score_loss(y,p)),
        "log_loss": float(log_loss(y, np.c_[1-p,p], labels=[0,1])),
        "accuracy_0.5": float(accuracy_score(y,(p>=0.5).astype(int))),
    }
    if len(np.unique(y)) > 1:
        out["roc_auc"] = float(roc_auc_score(y,p))
        out["average_precision"] = float(average_precision_score(y,p))
    else:
        out["roc_auc"] = None
        out["average_precision"] = None
    return out

def residual_summary(residuals):
    arr = residuals.to_numpy(dtype=float)
    out = {
        "mean_abs_residual": float(np.mean(np.abs(arr))),
        "residual_variance": float(np.var(arr)),
    }
    if len(residuals) > 2:
        vals = []
        for c in residuals.columns:
            s = residuals[c].to_numpy(dtype=float)
            if np.std(s[:-1]) > 0 and np.std(s[1:]) > 0:
                vals.append(np.corrcoef(s[:-1], s[1:])[0,1])
        out["mean_abs_lag1_autocorr"] = float(np.mean(np.abs(vals))) if vals else 0.0
    else:
        out["mean_abs_lag1_autocorr"] = 0.0
    return out
