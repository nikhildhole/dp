def iss(nums, target, n, dp):
    if(target == 0):
        return True
    if(n == 0):
        return False
    
    if(target < nums[n-1]):
        return iss(nums=nums, target=target, n=n-1, dp=dp)
    else:
        return iss(nums=nums, target=target, n=n-1, dp=dp) or iss(nums=nums, target=target-nums[n-1], n=n-1, dp=dp)



def is_subset_sum(nums, target):
    n = len(nums)
    
    # Step 1: Initialize the DP table
    dp = [[""] * (target + 1) for _ in range(n + 1)]

    # TODO: Fill in the DP initialization and transition
    return iss(nums, target,n, dp)

    
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
