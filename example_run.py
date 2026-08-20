import json
import pandas as pd
from raven import RAVENExperiment

df = pd.read_csv("example_data.csv")

exp = RAVENExperiment(
    time_column="time",
    target_column="future_event",
    signal_columns=["a","b","c"],
    horizons=(3,7,23),
    random_state=23,
)

result = exp.run(df)
print(json.dumps(result, indent=2))
