# Limitations and Scope

## 1. Historical event data is not player tracking

Fergie Time uses historical match-event data. It does not use:

- Optical player-tracking data.
- GPS tracking data.
- Measured player coordinates.

The application includes player lineups and player information, but its pitch visualization is schematic. It represents tactical arrangements and player roles rather than observed player locations. Ball position is derived from the game state rather than measured from tracking data. This distinction matters because event data and tracking data describe different aspects of football. Event data records selected actions. Tracking data can provide continuous information about player and ball movement.

## 2. Counterfactual outcomes are model-dependent

The application estimates possible futures under alternative tactical decisions. These are simulated outcomes, not observed outcomes. Their reliability depends on the assumptions and historical information used by the model. A simulation cannot establish what would certainly have happened if a team had made a different decision.

## 3. Historical conditions change

Football changes across seasons. The original diagnostics identified differences in:

- Added time.
- Late-match shot volume.
- Late-match expected goals.
- Substitution usage.
- Goals per expected goal.
- Home-points-per-match distributions.

A model calibrated on one period may not represent another period equally well. Temporal differences can affect both the data distribution and the relationship between match states and eventual outcomes.

## 4. Backtesting is not uniformly successful

The original historical evaluation identified discrepancies across multiple older-season match groups. The two most recent seasons (**2024/25, 2025/26**) used by the production daily pool passed the documented evaluation gate. Older seasons did not consistently satisfy it. This should not be generalized into a claim that the model passes every historical evaluation. The evaluation findings are summarized in [Evaluation and Historical Diagnostics](evaluation.md).

## 5. Monte Carlo uncertainty remains

Monte Carlo estimates are subject to sampling variability. Common random numbers can improve the precision of comparisons between candidate decisions when the paired outcomes are positively correlated. They do not eliminate simulation uncertainty. They also do not correct:

- Model misspecification.
- Data-quality problems.
- Distribution shift.
- Missing variables.
- Incorrect assumptions about tactical effects.

## 6. Event data does not capture every tactical factor

Historical event data does not fully represent many factors that influence real football, including:

- Off-ball movement.
- Defensive shape.
- Pressing intensity.
- Player fatigue.
- Communication.
- Tactical instructions as executed on the pitch.
- The spatial relationships between all players throughout a match.

These factors can influence real outcomes but are not directly observed in the event data used by this project.

## 7. Intended interpretation

Fergie Time is an interactive decision-simulation project and a demonstration of statistical modeling, uncertainty-aware comparison, and historical model evaluation. It should not be interpreted as:

- A professional player-recruitment model.
- A player-tracking analytics platform.
- A validated tactical recommendation system for professional clubs.
- A substitute for coaching judgment.

The project is best understood as an independent exploration of how simulation and statistical reasoning can help communicate decision trade-offs under uncertainty.