# RAVEN

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Raven) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Recursive Anomaly and Variance Evaluation Network**

RAVEN is an EFMW-derived residual-analysis framework.

Its job is not to discover exotic structure by default.

Its job is:

> Fit ordinary explanations first, measure what remains, and test whether the residual contains persistent predictive structure that survives controls.

## Intended uses

- anomaly residual analysis
- unexplained model error
- system-identification leftovers
- cross-model disagreement
- recurring forecast misses
- machine monitoring
- AI reliability
- scientific hypothesis generation

## Core signal path

```text
observations
→ conventional baseline model
→ residual
→ residual variance
→ recurrence
→ temporal persistence
→ cross-feature residual coupling
→ representation perturbation
→ residual predictiveness
→ RAVEN score
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
raven.py
features.py
baselines.py
metrics.py
freeze.py
residual_schema.json
example_config.yaml
example_data.csv
example_run.py
test_raven.py
MANIFEST.sha256
```

## Scientific hypothesis

> Some systems may contain residual structure that remains predictively useful after strong conventional structure has been removed.

RAVEN does not assume this is true.

## Required discipline

Before interpreting any residual as interesting:

- compare against strong baselines
- inspect autocorrelation
- inspect heteroskedasticity
- test shuffles
- test alternate representations
- check leakage
- verify out-of-sample predictiveness
- replicate

## Baselines

Included:

- linear baseline residual
- autoregressive residual
- raw-feature logistic predictor
- shuffled-residual control
- base-rate predictor

## Primary endpoint

> Does residual structure add out-of-sample predictive information beyond the baseline model that generated the residual?

Primary metric:

- Brier score

Secondary metrics:

- log loss
- ROC-AUC
- average precision
- residual autocorrelation
- residual variance
- residual recurrence
- shuffle sensitivity

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Minimal use

```python
import pandas as pd
from raven import RAVENExperiment

df = pd.read_csv("example_data.csv")

exp = RAVENExperiment(
    time_column="time",
    target_column="future_event",
    signal_columns=["a","b","c"],
    horizons=(3,7,23),
)

print(exp.run(df))
```

## Freeze discipline

Freeze before serious use:

- baseline model class
- residual definition
- feature set
- horizons
- recurrence rule
- shuffle control
- target
- split
- metric
- exclusions
- seeds

## Interpretation rule

A reproducible residual is not automatically a new mechanism.

It may reflect:

- omitted variables
- nonlinearities
- measurement artifacts
- regime changes
- misspecified baselines
- leakage
- known but unmodeled structure

RAVEN only establishes that something remains.

## Negative results

If residual features do not improve held-out prediction, the residual is not demonstrated to contain useful predictive information.

## Status

Research software. Experimental.
