# Evaluation and Historical Diagnostics

## 1. Evaluation objective

The historical backtest investigates whether the simulated continuation of a real match resembles the distribution of outcomes observed in historical matches. For each historical match situation, the evaluation process broadly follows this structure:

1. Construct a match state from historical match events.
2. Simulate the continuation from that state.
3. Compare simulated outcomes with the actual continuation.
4. Aggregate comparisons across match situations and seasons.
5. Inspect performance by relevant groups rather than relying only on pooled results.

The original evaluation considered:

- Win, draw, and loss outcomes.
- Late goals scored by each side.
- Calibration and probabilistic scoring metrics.
- Differences across match situations.
- Differences across seasons.

The objective is to assess the representativeness of the simulated environment. It is not, by itself, proof that a particular tactical decision is optimal.

## 2. Historical data coverage

The original project documentation reports the following coverage:

| Measure | Reported count |
|---|---:|
| Premier League seasons | 12 |
| Matches | 4,560 |
| Shots | 116,004 |
| Match situations | 12,599 |

The seasons cover **2014/15 through 2025/26**. The production daily pool uses the two most recent seasons. Older seasons are available as practice scenarios, rather than being treated as equivalent to the production daily pool. These counts are reproduced from the original project documentation. The underlying dataset and internal processing scripts are not included in this public showcase.

## 3. Backtesting approach

The backtest begins from a historical match state and simulates the remaining match under the default continuation policy. The original evaluation compares observed and simulated outcomes, including:

- Win, draw, and loss rates.
- Late goals for the team represented by the scenario.
- Late goals for the opponent.

The original evaluation gate uses standardized differences and minimum sample-size requirements. It also examines longer comeback situations by season. The purpose of the gate is to identify material discrepancies between simulated and observed outcomes. Passing an aggregate comparison does not establish that every subgroup is well represented. The exact internal gate implementation is not included in this repository.

## 4. Temporal diagnostics

The original season-level analysis identified changes in the match environment over time. Examples from the original diagnostics include:

- Mean last-shot timing increased from approximately 90 minutes in earlier seasons to approximately 93 minutes in some recent seasons.
- Goals from the 90th minute increased from approximately 0.13 per match in several earlier seasons to approximately 0.27 in 2023/24 and 2025/26.
- Substitution usage increased from roughly 2.7 to 3.0 per side in earlier seasons to roughly 3.9 to 4.2 in more recent seasons.
- The 2020/21 season had notably different home-points-per-match statistics, during the unusual empty-stadium period.

These are descriptive observations. They do not establish that any single rule change caused the differences. They do suggest that historical match conditions are not stationary. A model that represents one period reasonably well may not represent another period equally well.

## 5. Evaluation findings

The original documentation does not report a universal pass across all seasons. The main findings were:

- The pooled historical evaluation identified discrepancies in multiple match-situation groups.
- Older seasons showed systematic differences between simulated and observed late goals in some groups.
- The two most recent seasons used by the production daily pool passed the documented evaluation gate.
- Older seasons did not consistently satisfy that gate.
- A separate ten-season practice-pool report recorded 11 evaluation cells outside its gate-v2 limits.

The distinction between the recent daily pool and older practice scenarios is therefore important. The results do not support a claim that the model passed every historical evaluation.

| Evaluation population        | Result                                      | Interpretation                               |
| ---------------------------- | ------------------------------------------- | -------------------------------------------- |
| Recent two-season daily pool | Passed documented gate                      | Suitable for the documented daily-pool scope |
| Older-season practice pool   | 11 cells outside gate v2                    | Historical discrepancies remain              |
| Pooled practice scoring      | Better than climatology on reported metrics | Does not establish universal calibration     |

## 6. Pooled scoring metrics

The original practice-pool report included the following pooled scoring results:

| Metric | Engine | Climatology |
|---|---:|---:|
| Log loss | 0.574 | 0.597 |
| Brier score | 0.322 | 0.332 |

The report covered 7,068 pooled scenarios.

> **Climatology baseline:** A reference model that predicts outcomes using their historical average frequencies, without considering the specific match state or situation. It provides a simple benchmark for assessing whether the simulation model adds predictive value beyond historical base rates. 

These figures indicate that the engine achieved better pooled scores than the climatology baseline in that report. They do **not** establish universal calibration or reliable performance in every subgroup. Comparing the engine against climatology is useful because it tests whether the model captures meaningful match-state information rather than merely reproducing average outcome frequencies. Pooled metrics can conceal localized failure. The evaluation-gate discrepancies remain relevant even when aggregate scoring metrics look favorable.

## 7. How the findings affected project scope

* The historical evaluation influenced how the application treats its scenario pools.

* Rather than treating all seasons as interchangeable, the application distinguishes the recent daily pool from older practice scenarios.

* This is a practical example of why model evaluation should consider temporal and population differences. A model can perform reasonably in aggregate while exhibiting systematic errors in particular contexts.

## 8. Reproducibility and provenance

* The figures in this document are summarized from the original project's internal `BACKTESTING.md` and saved reports.

* The production data, simulation engine, and internal diagnostic scripts are intentionally excluded from this public showcase.

* The included [`historical-season-summary.csv`](../results/historical-season-summary.csv) contains selected descriptive season-level statistics. It does not contain raw match data or model predictions.

* The historical counts and evaluation metrics have not been independently reproduced from the original dataset within this public repository. They should be interpreted as reported results from the original project documentation.