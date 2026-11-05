# Evaluation and Historical Diagnostics

## Evaluation objective

The purpose of the historical backtest is to test whether the simulated continuation resembles the distribution of outcomes observed in real matches.

For each historical match situation:

1. Construct the match state from the real match.
2. Simulate the continuation from that state.
3. Compare simulated outcomes with the actual continuation.
4. Aggregate the comparisons across match situations and seasons.

The evaluation considers:

- Win, draw, and loss rates
- Late goals scored by each side
- Calibration and scoring metrics
- Performance across different match situations
- Performance across seasons

## Historical data coverage

The original project documentation reports:

| Measure | Count |
|---|---:|
| Premier League seasons | 12 |
| Matches | 4,560 |
| Shots | 116,004 |
| Match situations | 12,599 |

The seasons cover **2014/15 through 2025/26.** The production daily pool uses the two most recent seasons. Older seasons are available as practice scenarios, not as part of the daily pool.

## Backtesting methodology

The backtest begins from the real match state and simulates the remaining match under the default continuation policy. The comparison includes observed and simulated:

- Win, draw, and loss rates
- Late goals for the managed side
- Late goals for the opponent

The original gate uses standardized differences and minimum sample-size requirements. It also evaluates longer comeback situations by season. The purpose is not to prove that a particular tactical decision is optimal. It is to test whether the simulated environment is sufficiently representative of historical outcomes for decision comparisons to be meaningful.

## What the historical diagnostics revealed

The original analysis found that the simulated late-goal rate was relatively stable across seasons, while the observed rate varied substantially. Examples from the original season-level diagnostics:

- The mean last-shot minute increased from approximately 90 to approximately 93 minutes in more recent seasons.
- Goals from the 90th minute increased from approximately 0.13 per match in several earlier seasons to approximately 0.27 in 2023/24 and 2025/26.
- Substitution usage increased from roughly 2.7 to 3.0 per side in earlier seasons to roughly 3.9 to 4.2 in more recent seasons.
- The 2020/21 season had notably different home-points-per-match statistics, consistent with the unusual empty-stadium context.

These findings suggested that the match environment changed over time and that a single set of assumptions could fail to represent every era equally well.

## Evaluation results and limitations

* The original documentation does not report a universal pass across all seasons.

* The pooled historical evaluation identified discrepancies in multiple match-situation groups. In particular, older seasons showed systematic differences between simulated and observed late goals.

* The two most recent seasons used by the shipped daily pool passed the documented gate, while the older seasons did not consistently satisfy it.

* The separate ten-season practice-pool report also records 11 cells outside its gate-v2 limits.

* This is important: **a better aggregate score does not erase failures in particular groups or seasons.**

## Scoring metrics

The practice-pool report includes pooled scoring results:

| Metric | Engine | Climatology |
|---|---:|---:|
| Log loss | 0.574 | 0.597 |
| Brier score | 0.322 | 0.332 |

These figures cover 7,068 pooled scenarios in that report. They are useful comparative diagnostics, but they do not establish that every situation is well calibrated. The gate failures remain relevant.

## Why this matters

The evaluation work influenced the product's scope. Rather than treating every historical season as interchangeable, the application distinguishes the recent daily pool from older practice scenarios. The broader lesson is that a model can look reasonable in aggregate while failing systematically in particular populations or contexts.

## Reproducibility and provenance

* The figures in this document are summarized from the original project's `BACKTESTING.md` and saved reports.

* The production data, engine implementation, and internal diagnostic scripts are intentionally not included in this public showcase.

* The included CSV provides selected descriptive season-level diagnostics, not raw match data or model predictions.