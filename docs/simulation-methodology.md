# Simulation Methodology

## 1. Problem formulation

Given a match state and a set of legal tactical decisions, let's estimate the distribution of possible outcomes under each decision. The goal is to compare decisions under uncertainty rather than assume that one simulated outcome represents what would actually happen. Each candidate decision produces a distribution over:

- Win
- Draw
- Loss

## 2. Monte Carlo simulation

Monte Carlo simulation estimates outcome probabilities by repeatedly sampling possible continuations. For a candidate decision, let's define:

- $P(W)$ is the probability of winning.
- $P(D)$ is the probability of drawing.
- $P(L)$ is the probability of losing.

The outcome probabilities satisfy:

$$P(W) + P(D) + P(L) = 1$$

Expected points are:

$$EP = 3P(W) + P(D)$$

This follows the standard football points system: 
* $3$ points for a win
* $1$ point for a draw
* $0$ point for a loss

If $N$ simulations produce $N_W$ wins, $N_D$ draws, and $N_L$ losses, the estimated probabilities are:

$$
\begin{aligned}
\widehat{P}(W) &= \frac{N_W}{N} \\
\widehat{P}(D) &= \frac{N_D}{N} \\
\widehat{P}(L) &= \frac{N_L}{N}
\end{aligned}
$$


The estimated expected points are:

$$
\widehat{EP} = 3\widehat{P(W)} + \widehat{P(D)}
$$

The production application is documented as evaluating each legal option with 1,000 simulations. Monte Carlo estimates are approximations. Increasing the number of simulations generally reduces sampling error, but it does not correct a misspecified model or unrepresentative historical data.

## 3. Comparing candidate decisions

Suppose two candidate decisions, $A$ and $B$, produce estimated expected points:

$$
\widehat{EP}_A \quad \text{and} \quad \widehat{EP}_B
$$

Their estimated difference is:

$$
\widehat{\Delta} = \widehat{EP}_A - \widehat{EP}_B
$$

A positive value favors $A$ on expected points. A negative value favors $B$. However, the estimated difference is itself uncertain because both expected points estimates are based on finite simulations. A comparison should therefore consider the uncertainty of the difference, not just the difference in point estimates.

## 4. Common random numbers

A naive comparison may simulate candidate decisions using unrelated random draws. That can introduce unnecessary Monte Carlo noise into the difference between the estimates. Common random numbers (CRN) address this by using shared random inputs across candidate decisions. This creates paired simulation outcomes. For simulation $i$, let:

$$X_i = \text{outcome under decision A} $$

$$Y_i = \text{outcome under decision B}$$

The paired difference is:

$$D_i = X_i - Y_i$$

The estimated difference is:

$$\bar D = \frac{1}{N}\sum_{i=1}^{N}D_i$$

The standard error of the paired estimate is:

$$SE(\bar{D}) = \frac{s_D}{\sqrt{N}}$$

where $s_D$ is the sample standard deviation of the paired differences. The statistical reason CRN can help is:

$$
\operatorname{Var}(X-Y) =
\operatorname{Var}(X) +
\operatorname{Var}(Y) -
2\operatorname{Cov}(X,Y)
$$

When the shared random inputs induce positive covariance between the candidate outcomes, the variance of their difference can be smaller than it would be under independent simulation. This variance reduction is not guaranteed for every model or every pair of decisions. The random inputs must also be aligned meaningfully across candidates. If candidate policies consume random inputs inconsistently, the intended pairing may be weakened or invalidated. CRN reduces noise in a comparison. It does not make the underlying model more accurate.

## 5. Uncertainty-aware rankings

A small numerical difference should not automatically imply that one decision is inferior. When the estimated difference is small relative to its uncertainty, the evidence may not support a meaningful ranking. A common approximate interval for a paired difference is:

$$\bar{D} \pm 1.96 \times SE(\bar{D})$$

This is a normal-approximation interval. Its interpretation depends on the simulation design and the adequacy of the approximation. If the interval includes $0$, the observed difference is not clearly distinguishable from simulation noise at the corresponding approximate confidence level. That does not prove that the decisions are identical. It means the available simulation evidence does not clearly separate them. The production implementation uses its own state-level comparison and tie-handling logic. The exact implementation details are not reproduced here.

## 6. Statistical versus practical significance

A difference can be statistically distinguishable yet too small to matter in practice. Conversely, a potentially meaningful difference may be estimated imprecisely. It is useful to distinguish between:

- **Statistical uncertainty:** How much could the estimated difference vary because of finite simulation sampling?
- **Practical significance:** Is the estimated difference large enough to matter for the decision?

The production application documents practical-significance thresholds for its decision grading. Those thresholds are implementation-specific and are not required to understand the general methodology.

## 7. Multi-objective reporting

Expected points provide a useful summary, but they do not capture every trade-off. For example, one decision may increase the chance of winning while also increasing the chance of losing. The application therefore reports several quantities:

- Expected points
- Win probability
- Draw probability
- Loss probability
- Outcome variability
- Differences between candidate decisions

This makes the trade-off between a safer outcome distribution and a more volatile one easier to inspect.

## 8. Standalone examples

The `examples/` directory contains independent Python demonstrations of:

- Monte Carlo estimation of win, draw, and loss probabilities.
- Expected-points estimation and Monte Carlo standard error.
- Paired comparisons using common random numbers.
- Comparison with independent simulation.

The examples use synthetic probabilities. They illustrate the statistical ideas without reproducing the production engine or its parameters.