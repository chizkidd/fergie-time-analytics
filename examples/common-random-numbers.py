"""
Common random numbers: an illustrative paired simulation.

Demonstrates:
- Why paired simulation can improve comparisons between decisions.
- How common random numbers create paired outcomes.
- How to calculate the standard error of paired differences.
- How paired and independent comparisons can differ in precision.

Uses illustrative probabilities, not production Fergie Time parameters.

This is a simplified categorical example. In a real simulation, shared
random inputs must be consumed consistently by candidate policies for
the pairing to be meaningful.

Variance reduction is not guaranteed for every model or every pair
of decisions.

This version includes probability validation and guards 
against division by zero when reporting the standard-error ratio.
"""

import numpy as np


N_SIMULATIONS = 100_000
SEED = 42

# Outcome order: win, draw, loss.
DECISION_A = np.array([0.35, 0.40, 0.25])
DECISION_B = np.array([0.40, 0.32, 0.28])

# Expected-points scoring.
OUTCOME_POINTS = np.array([3.0, 1.0, 0.0])


def validate_probabilities(probabilities):
    """Check that probabilities form a valid categorical distribution."""
    probabilities = np.asarray(probabilities, dtype=float)

    if probabilities.shape != (3,):
        raise ValueError("Expected exactly three probabilities: win, draw, loss.")

    if not np.all(np.isfinite(probabilities)):
        raise ValueError("Probabilities must be finite.")

    if np.any(probabilities < 0):
        raise ValueError("Probabilities cannot be negative.")

    if not np.isclose(probabilities.sum(), 1.0):
        raise ValueError("Probabilities must sum to 1.")

    return probabilities


def sample_points(uniforms, probabilities):
    """
    Convert uniform random draws into football outcome points.

    Categories:
        [0, p_win)                  -> win
        [p_win, p_win + p_draw)     -> draw
        remaining interval          -> loss
    """
    probabilities = validate_probabilities(probabilities)

    outcomes = np.searchsorted(
        np.cumsum(probabilities),
        uniforms,
        side="right",
    )

    return OUTCOME_POINTS[outcomes]


def summarize(values):
    """Return the sample mean and standard error."""
    values = np.asarray(values, dtype=float)

    if values.ndim != 1 or len(values) < 2:
        raise ValueError("At least two one-dimensional observations are required.")

    return {
        "mean": values.mean(),
        "standard_error": values.std(ddof=1) / np.sqrt(len(values)),
    }


def main():
    rng = np.random.default_rng(SEED)

    # Generate one random tape shared by both decisions.
    shared_uniforms = rng.random(N_SIMULATIONS)

    points_a = sample_points(shared_uniforms, DECISION_A)
    points_b = sample_points(shared_uniforms, DECISION_B)

    # Paired comparison.
    paired_differences = points_a - points_b
    paired_result = summarize(paired_differences)

    result_a = summarize(points_a)
    result_b = summarize(points_b)

    # Independent sampling comparison.
    independent_a = sample_points(
        rng.random(N_SIMULATIONS),
        DECISION_A,
    )

    independent_b = sample_points(
        rng.random(N_SIMULATIONS),
        DECISION_B,
    )

    independent_differences = independent_a - independent_b
    independent_result = summarize(independent_differences)

    print(f"Simulations: {N_SIMULATIONS:,}\n")

    print("Decision A")
    print(f"  Expected points: {result_a['mean']:.4f}")

    print("\nDecision B")
    print(f"  Expected points: {result_b['mean']:.4f}")

    print("\nPaired comparison using common random numbers")
    print(f"  Difference A - B: {paired_result['mean']:.4f}")
    print(f"  Standard error:   {paired_result['standard_error']:.5f}")

    print("\nIndependent comparison")
    print(f"  Difference A - B: {independent_result['mean']:.4f}")
    print(f"  Standard error:   {independent_result['standard_error']:.5f}")

    paired_se = paired_result["standard_error"]
    independent_se = independent_result["standard_error"]

    print("\nStandard-error comparison")

    if paired_se == 0:
        print("  Paired standard error is zero; ratio is undefined.")
    else:
        ratio = independent_se / paired_se
        print(f"  Independent SE / paired SE: {ratio:.2f}x")


if __name__ == "__main__":
    main()

# SOLUTION:
# Simulations: 100,000

# Decision A
#   Expected points: 1.4475

# Decision B
#   Expected points: 1.5155

# Paired comparison using common random numbers
#   Difference A - B: -0.0680
#   Standard error:   0.00149

# Independent comparison
#   Difference A - B: -0.0634
#   Standard error:   0.00552

# Standard-error comparison
#   Independent SE / paired SE: 3.70x
