public class PartitionEqualSum {
    
    /**
     * TODO: Implement this method
     * 
     * Problem: Given a non-empty array of positive integers, determine if the array 
     * can be partitioned into two subsets such that the sum of elements in both 
     * subsets is equal.
     * 
     * @param nums array of positive integers
     * @return true if array can be partitioned into two equal sum subsets, false otherwise
     * 
     * Example:
     * Input: [1, 5, 11, 5]
     * Output: true (can be partitioned as [1, 5, 5] and [11])
     * 
     * Input: [1, 2, 3, 5]
     * Output: false (cannot be partitioned into equal sum subsets)
     */
    public static boolean canPartition(int[] nums) {
        // TODO: Write your solution here
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
        }
        if(sum % 2 != 0){
            return  false;
        }

        return cP(nums, sum/2, nums.length);
    }

    public static boolean cP(int[] nums, int sum, int i){
        if(sum == 0){
            return true;
        }
        if(i == 0){
            return false;
        }

        if(sum < nums[i-1]){
            return cP(nums, sum, i-1);
        }else{
            return cP(nums, sum, i-1) || cP(nums, sum - nums[i-1], i-1);
        }
    }
    
    // Test cases
    public static void main(String[] args) {
        System.out.println("Testing Partition Equal Sum Problem");
        System.out.println("===================================");
        
        // Test Case 1: Basic case - can be partitioned
        int[] test1 = {1, 5, 11, 5};
        boolean result1 = canPartition(test1);
        System.out.println("Test 1: [1, 5, 11, 5]");
        System.out.println("Expected: true, Got: " + result1);
        System.out.println("Status: " + (result1 == true ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 2: Cannot be partitioned
        int[] test2 = {1, 2, 3, 5};
        boolean result2 = canPartition(test2);
        System.out.println("Test 2: [1, 2, 3, 5]");
        System.out.println("Expected: false, Got: " + result2);
        System.out.println("Status: " + (result2 == false ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 3: Single element - cannot partition
        int[] test3 = {5};
        boolean result3 = canPartition(test3);
        System.out.println("Test 3: [5]");
        System.out.println("Expected: false, Got: " + result3);
        System.out.println("Status: " + (result3 == false ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 4: Two elements - equal
        int[] test4 = {1, 1};
        boolean result4 = canPartition(test4);
        System.out.println("Test 4: [1, 1]");
        System.out.println("Expected: true, Got: " + result4);
        System.out.println("Status: " + (result4 == true ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 5: Two elements - not equal
        int[] test5 = {1, 3};
        boolean result5 = canPartition(test5);
        System.out.println("Test 5: [1, 3]");
        System.out.println("Expected: false, Got: " + result5);
        System.out.println("Status: " + (result5 == false ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 6: Larger array - can be partitioned
        int[] test6 = {1, 2, 3, 4, 5, 6, 7};
        boolean result6 = canPartition(test6);
        System.out.println("Test 6: [1, 2, 3, 4, 5, 6, 7]");
        System.out.println("Expected: true, Got: " + result6);
        System.out.println("Status: " + (result6 == true ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 7: All same elements - even count
        int[] test7 = {2, 2, 2, 2};
        boolean result7 = canPartition(test7);
        System.out.println("Test 7: [2, 2, 2, 2]");
        System.out.println("Expected: true, Got: " + result7);
        System.out.println("Status: " + (result7 == true ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 8: All same elements - odd count
        int[] test8 = {3, 3, 3};
        boolean result8 = canPartition(test8);
        System.out.println("Test 8: [3, 3, 3]");
        System.out.println("Expected: false, Got: " + result8);
        System.out.println("Status: " + (result8 == false ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 9: Large numbers
        int[] test9 = {100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200};
        boolean result9 = canPartition(test9);
        System.out.println("Test 9: Array with 24 hundreds and one 200");
        System.out.println("Expected: true, Got: " + result9);
        System.out.println("Status: " + (result9 == true ? "PASS" : "FAIL"));
        System.out.println();
        
        // Test Case 10: Edge case - sum is odd
        int[] test10 = {1, 2, 5};
        boolean result10 = canPartition(test10);
        System.out.println("Test 10: [1, 2, 5]");
        System.out.println("Expected: false, Got: " + result10);
        System.out.println("Status: " + (result10 == false ? "PASS" : "FAIL"));
        System.out.println();
        
        System.out.println("All tests completed!");
    }
}