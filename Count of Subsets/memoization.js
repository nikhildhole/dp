function csws(nums, target, sum, i, n, arr){
    if(n == i){
        return target === sum ? 1 : 0
    }
    if(arr[i][sum] !== undefined){
        return arr[i][sum]
    }
    var exlcude = csws(nums, target, sum, i + 1,  n, arr)

    var inlcude = csws(nums, target, sum + nums[i], i + 1,  n, arr)

    arr[i][sum] = exlcude + inlcude
    return arr[i][sum]
}

function countSubsetsWithSum(nums, target) {
    // TODO: Implement this function
    arr = Array.from(Array(nums.length+1), () => new Array(target+1))

    return csws(nums, target, 0, 0, nums.length, arr)
}


// Test cases
const tests = [
    { nums: [1, 2, 3], target: 4, expected: 1 }, // Only [1,3]
    { nums: [1, 1, 1, 1], target: 2, expected: 6 }, // Many ways to pick two 1s
    { nums: [2, 3, 5, 6, 8, 10], target: 10, expected: 3 }, // [2,8], [10], [5,3,2]
    { nums: [1, 2, 7, 1, 5], target: 9, expected: 3 },
    { nums: [], target: 0, expected: 1 }, // Empty subset is valid
    { nums: [], target: 5, expected: 0 }, // No subset possible
];

tests.forEach(({ nums, target, expected }, idx) => {
    const result = countSubsetsWithSum(nums, target);
    console.log(`Test ${idx + 1}:`, result === expected ? '✅ Passed' : `❌ Failed (Expected ${expected}, got ${result})`);
});
