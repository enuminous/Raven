# RAVEN

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Raven) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core signal path](#core-signal-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Required discipline](#required-discipline)
- [Baselines](#baselines)
- [Primary endpoint](#primary-endpoint)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Minimal use](#minimal-use)
- [Freeze discipline](#freeze-discipline)
- [Interpretation rule](#interpretation-rule)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Dolphin](https://github.com/enuminous/Dolphin) · [Spider](https://github.com/enuminous/Spider) · [Ant](https://github.com/enuminous/Ant) · [Fox](https://github.com/enuminous/Fox)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
