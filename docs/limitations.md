# Limitations and Scope

## 1. Historical event data is not player tracking

Fergie Time uses historical match-event data. It does not use optical tracking data, GPS tracking, or measured player coordinates. The application includes player lineups and player roles, but the pitch visualization is schematic. It represents tactical arrangements and player roles rather than observed player locations. Ball position is also derived from the game state, not measured from tracking data.

## 2. Counterfactuals are model-dependent

The application estimates possible futures under alternative tactical decisions. These are simulated outcomes, not observed outcomes. Their reliability depends on the assumptions and historical information used by the model. A simulation cannot establish what would certainly have happened if a team had made a different decision.

## 3. Historical conditions change

Football changes across seasons. The original diagnostics identified differences in:

- Added time
- Late-match shot volume
- Late-match expected goals
- Substitution usage
- Goals per expected goal
- Home-points-per-match distributions

A model calibrated on one period may not represent another period equally well.

## 4. Backtesting is not uniformly successful

The original historical evaluation identified discrepancies across multiple older-season match groups. The recent seasons used by the shipped daily pool passed the documented gate, but this should not be generalized into a claim that the model passes every historical evaluation.

## 5. Simulation uncertainty remains

Monte Carlo estimates are subject to sampling variability. Common random numbers can improve the precision of comparisons between candidate decisions, but they do not eliminate uncertainty or correct model misspecification.

## 6. Event data does not capture every tactical factor

Historical event data does not fully represent:

- Off-ball movement
- Defensive shape
- Pressing intensity
- Player fatigue
- Communication
- Tactical instructions as executed on the pitch

These factors can influence real football outcomes but are not directly observed in the available event data.

## 7. Intended interpretation

Fergie Time is an interactive decision-simulation gaming project and a demonstration of statistical modeling, uncertainty-aware comparison, and historical model evaluation. It should not be interpreted as a professional recruitment model, a player-tracking analytics platform, or a substitute for coaching judgment.