def knapsack(weights, values, capacity, n, dp):
    """
    Recursive function to solve 0/1 Knapsack using memoization.

    Parameters:
        weights: list of item weights
        values: list of item values
        capacity: maximum capacity of knapsack
        n: number of items
        dp: 2D list for memoization

    Returns:
        Maximum value that can be obtained
    """

    # Your implementation goes here
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if n == 0 or capacity == 0:
        return 0
    
    if capacity < weights[n-1]:
        dp[n][capacity] = knapsack(weights=weights, values=values, capacity=capacity, n=n-1, dp=dp)
    else:
        exclude = knapsack(weights=weights, values=values, capacity=capacity, n=n-1, dp=dp)
        include = values[n-1] + knapsack(weights=weights, values=values, capacity=capacity-weights[n-1], n=n-1, dp=dp)
        dp[n][capacity] = max(exclude, include)

    return dp[n][capacity]

def test_knapsack():
    weights = [1, 3, 4, 5]
    values = [10, 40, 50, 70]
    capacity = 8
    n = len(weights)

    # Initialize dp array with -1
    dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

    result = knapsack(weights, values, capacity, n, dp)
    expected = 110  # Optimal is items with weight 3 and 5 (40 + 70)

    print("Output:", result)
    print("Expected:", expected)
    print("✅ Correct" if result == expected else "❌ Incorrect")


# Run test
test_knapsack()
