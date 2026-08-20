import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler

class LogisticModel:
    def __init__(self, random_state=23):
        self.scaler = RobustScaler()
        self.model = LogisticRegression(max_iter=4000, random_state=random_state)
        self.constant_ = None

    def fit(self, X, y):
        y = np.asarray(y, dtype=int)
        if len(np.unique(y)) < 2:
            self.constant_ = float(y.mean()) if len(y) else 0.0
            return self
        self.scaler.fit(X)
        self.model.fit(self.scaler.transform(X), y)
        return self

    def predict_proba(self, X):
        if self.constant_ is not None:
            return np.full(len(X), self.constant_)
        return self.model.predict_proba(self.scaler.transform(X))[:,1]

class BaseRateModel:
    def fit(self, X, y):
        self.p_ = float(np.mean(y))
        return self
    def predict_proba(self, X):
        return np.full(len(X), self.p_, dtype=float)

def autoregressive_features(df, signal_columns):
    x = df[signal_columns].astype(float).ffill().fillna(0.0)
    out = pd.DataFrame(index=df.index)
    for c in signal_columns:
        out[c] = x[c]
        out[f"{c}__lag1"] = x[c].shift(1).fillna(0.0)
        out[f"{c}__lag2"] = x[c].shift(2).fillna(0.0)
    return out.fillna(0.0)
