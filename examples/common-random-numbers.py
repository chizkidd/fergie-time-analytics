"""
Common random numbers: an illustrative paired simulation.
- Why paired simulation can make comparisons between decisions more precise.

The two hypothetical decisions are evaluated using the same
uniform random numbers for each simulation index.

This creates paired outcomes and allows the comparison to use
the standard error of the paired differences.

Uses illustrative probabilities, not production Fergie Time parameters.

Note: This illustration uses a deliberately simplified categorical outcome model. 
In a real simulation, the shared random tape must be consumed consistently by the 
candidate policies for the pairing to be meaningful. The variance reduction is not 
guaranteed for every model or every pair of decisions.
"""

import numpy as np


N_SIMULATIONS = 100_000
SEED = 42

# Illustrative win/draw/loss probabilities.
DECISION_A = np.array([0.35, 0.40, 0.25])
DECISION_B = np.array([0.40, 0.32, 0.28])

# Expected-points scoring.
OUTCOME_POINTS = np.array([3.0, 1.0, 0.0])


def sample_points(uniforms, probabilities):
    """
    Convert uniform random draws into football outcome points.

    Categories:
        [0, p_win)                  -> win
        [p_win, p_win + p_draw)     -> draw
        remaining interval          -> loss
    """
    if not np.isclose(probabilities.sum(), 1.0):
        raise ValueError("Probabilities must sum to 1.")

    cumulative = np.cumsum(probabilities)

    outcomes = np.searchsorted(
        cumulative,
        uniforms,
        side="right",
    )

    return OUTCOME_POINTS[outcomes]


def summarize(values):
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
    differences = points_a - points_b

    result_a = summarize(points_a)
    result_b = summarize(points_b)
    paired_result = summarize(differences)

    # Independent sampling as a comparison.
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

    print("\nVariance reduction")
    ratio = (
        independent_result["standard_error"]
        / paired_result["standard_error"]
    )

    print(f"  Independent SE / paired SE: {ratio:.2f}x")


if __name__ == "__main__":
    main()