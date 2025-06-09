def is_subset_sum(nums, target):
    n = len(nums)
    
    # Step 1: Initialize the DP table
    pre = [False] * (target + 1)
    pre[0] = True
    curr = [False] * (target + 1)


    for i in range(1, n+1):
        curr[0] = True
        for j in range(1, target+1):
            if nums[i-1] > j:
                curr[j] = pre[j]
            else:
                curr[j] = pre[j] or pre[j - nums[i-1]]
        pre = curr.copy()


    return pre[target]
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
