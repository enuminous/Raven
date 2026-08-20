import pandas as pd
from features import build_raven_features
from raven import RAVENExperiment

def test_features():
    df = pd.read_csv("example_data.csv")
    rf, residuals = build_raven_features(
        df, ["a","b","c"], train_end=250, horizons=(3,7,23), random_state=23
    )
    assert len(rf) == len(df)
    assert len(residuals) == len(df)
    assert "raven_residual_score" in rf.columns
    assert rf["raven_residual_score"].between(0,1).all()

def test_experiment_runs():
    df = pd.read_csv("example_data.csv")
    exp = RAVENExperiment(
        time_column="time",
        target_column="future_event",
        signal_columns=["a","b","c"],
    )
    out = exp.run(df)
    assert "results" in out
    assert "raven" in out["results"]
    assert "shuffled_residual" in out["results"]
