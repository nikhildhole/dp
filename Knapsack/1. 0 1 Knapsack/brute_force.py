def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0

    for i in range(2 ** n):  # loop through all combinations
        total_weight = 0
        total_value = 0
        for j in range(n):
            if (i >> j) & 1:  # check if j-th item is included
                total_weight += weights[j]
                total_value += values[j]
        if total_weight <= capacity:
            max_value = max(max_value, total_value)
    
    return max_value

# Example
weights = [3, 2, 4]
values = [60, 100, 120]
capacity = 5
print(knapsack_brute_force(weights, values, capacity))  # Output: 160
