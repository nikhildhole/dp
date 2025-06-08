def knapsack_iterative(weights, values, capacity):
    """
    Iterative DP solution for 0/1 Knapsack.

    Parameters:
        weights: list of item weights
        values: list of item values
        capacity: total knapsack capacity

    Returns:
        Maximum total value that fits in the knapsack
    """

    n = len(weights)
    # Create DP table (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 🚧 Your implementation goes here
    for number_of_elements in range(1, n+1):
        for current_max_weight in range(1, capacity+1):
            previous_row = number_of_elements-1
            current_weigth = weights[previous_row]
            previous_row_max_value = dp[previous_row][current_max_weight]
            if current_max_weight < current_weigth: # compare max capacity vs current select item weigth
                # if current weight is greater
                dp[number_of_elements][current_max_weight] = previous_row_max_value
            else:
                # if current weight is smaller
                current_value = values[previous_row]
                current_max_weight_after_current_weigth_mins = current_max_weight - current_weigth
                max_value_when_current_weight_mins = dp[previous_row][current_max_weight_after_current_weigth_mins] + current_value
                dp[number_of_elements][current_max_weight] = max(previous_row_max_value, max_value_when_current_weight_mins) 
    return dp[n][capacity]


def run_tests():
    test_cases = [
        {
            "weights": [1, 3, 4, 5],
            "values": [10, 40, 50, 70],
            "capacity": 8,
            "expected": 110
        },
        {
            "weights": [2, 3, 5],
            "values": [20, 30, 60],
            "capacity": 5,
            "expected": 60
        },
        {
            "weights": [5, 6, 7],
            "values": [10, 20, 30],
            "capacity": 4,
            "expected": 0
        },
        {
            "weights": [1, 2, 3],
            "values": [10, 20, 30],
            "capacity": 6,
            "expected": 60
        },
        {
            "weights": [3, 2, 2],
            "values": [60, 100, 120],
            "capacity": 4,
            "expected": 220
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = knapsack_iterative(test["weights"], test["values"], test["capacity"])
        print(f"Test Case {i}: Output = {result}, Expected = {test['expected']}")
        print("✅ Pass" if result == test["expected"] else "❌ Fail")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
