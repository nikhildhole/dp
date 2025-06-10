function countSubsetsWithSum(nums, target) {
    // TODO: Implement this function

    var arr = Array.from(Array(nums.length+1), () => new Array(target+1).fill(0))

    for(var i = 0; i < arr.length; i++){
        arr[i][0] = 1
    }

    arr[0][0] = 1

    for(var i = 1; i < nums.length+1; i++){
        for(var j = 1; j < target+1; j++){ 
            arr[i][j] = arr[i - 1][j]
            if(j >= nums[i-1]){
                arr[i][j] += arr[i - 1][j - nums[i - 1]]
            }
        }   
    }

    return arr[nums.length][target]
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
