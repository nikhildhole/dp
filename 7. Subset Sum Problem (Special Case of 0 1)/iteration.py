def is_subset_sum(nums, target):
    n = len(nums)
    
    # Step 1: Initialize the DP table
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # TODO: Fill in the DP initialization and transition

    # Base Case: sum 0 is possible with all item sets
    for i in range(n + 1):
        dp[i][0] = True

    for number_of_items in range(1, n+1):
        for max_sum in range(1, target+1):
            if max_sum < nums[number_of_items-1]:
                dp[number_of_items][max_sum] = dp[number_of_items-1][max_sum]
            else:
                dp[number_of_items][max_sum] = dp[number_of_items-1][max_sum] or dp[number_of_items-1][max_sum - nums[number_of_items-1]]

    return dp[n][target]
    # return True

# ✅ Test Cases
def test_is_subset_sum():
    assert is_subset_sum([2, 3, 7, 8, 10], 11) == True   # 3 + 8
    assert is_subset_sum([1, 2, 3], 7) == False
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 9) == True  # 4 + 5
    assert is_subset_sum([], 0) == True  # empty subset
    assert is_subset_sum([], 1) == False
    assert is_subset_sum([1], 1) == True
    assert is_subset_sum([1, 1, 1, 1], 2) == True

    print("✅ All test cases passed!")

# Run the test
test_is_subset_sum()
