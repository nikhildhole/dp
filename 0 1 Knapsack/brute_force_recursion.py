def knapsack_recursive(i, W, weights, values):
    # Base case: no items or no capacity left
    if i < 0 or W == 0:
        return 0

    # If item doesn't fit, skip it
    if weights[i] > W:
        return knapsack_recursive(i - 1, W, weights, values)
    
    # Otherwise, choose max of include vs exclude
    include = values[i] + knapsack_recursive(i - 1, W - weights[i], weights, values)
    exclude = knapsack_recursive(i - 1, W, weights, values)
    
    return max(include, exclude)

# Example
weights = [3, 2, 4]
values = [60, 100, 120]
capacity = 5
n = len(weights)
print(knapsack_recursive(n - 1, capacity, weights, values))  # Output: 160
