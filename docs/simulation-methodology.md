
# Simulation Methodology

## Problem formulation

Given a match state and a set of legal tactical decisions, estimate the distribution of possible outcomes under each decision. The objective is to compare decisions under uncertainty rather than assume that one simulated outcome is representative of what would happen.

## Monte Carlo simulation

For a candidate decision, the engine simulates the remainder of the match repeatedly. Each simulation produces a possible outcome:

- Win
- Draw
- Loss

Expected points are calculated as:

$$[EP = 3P(W) + P(D)]$$

where:

- $P(W)$ is the probability of winning.
- $P(D)$ is the probability of drawing.
- $P(L)$ is the probability of losing.
- $\sum{P(W) + P(D) + P(L) = 1}$

The application evaluates each legal option using 1,000 simulations.

## Common random numbers

A naive comparison might simulate each candidate decision using unrelated random draws. That introduces unnecessary Monte Carlo noise into the comparison. Instead, the application uses common random numbers: candidate decisions are evaluated using the same underlying random tape for each simulation index. This creates paired observations.

For simulation ($i$), let:

$$X_i = \text{outcome under decision A} $$

$$Y_i = \text{outcome under decision B}$$

The comparison uses:

$$D_i = X_i - Y_i$$

The estimated difference is:

$$\bar D = \frac{1}{N}\sum_{i=1}^{N}D_i$$

Its standard error is:

$$SE(\bar D) = \frac{s_D}{\sqrt{N}}$$

where $s_D$ is the sample standard deviation of the paired differences. The purpose is to reduce variance in the comparison, not to make the underlying simulation itself more accurate.

## Explicit tie bands

A small estimated difference should not automatically imply that one decision is inferior. The application uses a paired uncertainty estimate to identify decisions that are statistically indistinguishable from the best available option. The documented convention is:

$$|\Delta| \leq 1.96 \times SE$$

where $\Delta$ is the estimated difference from the best option and the standard error $(SE)$ is based on paired simulation results. The implementation uses a state-level band based on the widest paired standard error among legal calls. This avoids treating a noisy ranking as a meaningful distinction.

## Practical significance

Statistical uncertainty is not the only consideration. The application also uses a practical-significance floor:

- 0.02 expected points when grading on expected points.
- 0.5 percentage points of win probability when grading on win probability.

A decision inside the uncertainty band or below the practical-significance floor can be treated as equivalent to the best option.

## Multi-objective reporting

Expected points provide a common objective, but they do not communicate every trade-off. The report also exposes:

- Win probability
- Draw probability
- Loss probability
- Outcome variance
- Stake per outcome

This makes it possible to see when an option increases the chance of winning while also increasing the chance of losing.

## Standalone examples

The `examples/` directory contains independent Python demonstrations of Monte Carlo simulation and common random numbers. They use synthetic outcome probabilities. They illustrate the statistical ideas without reproducing the production engine.