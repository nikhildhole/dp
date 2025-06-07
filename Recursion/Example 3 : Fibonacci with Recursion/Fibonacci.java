public class Fibonacci {

    /**
     * Calculate the nth Fibonacci number using recursion.
     * 
     * Fibonacci sequence:
     * fib(0) = 0
     * fib(1) = 1
     * fib(n) = fib(n-1) + fib(n-2)
     * 
     * @param n Position in Fibonacci sequence
     * @return nth Fibonacci number
     * @throws IllegalArgumentException if n is negative
     */
    public static int fibonacci(int n) throws IllegalArgumentException {
        // TODO: Implement recursive logic here
        if (n < 0){
            throw new IllegalArgumentException("N should be greater than 0");
        } else if (n == 0){
            return 0;
        } else if (n == 1){
            return 1;
        } else if (n == 2){
            return 1;
        } else if (n == 3){
            return 2;
        }

        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    // Test runner
    public static void main(String[] args) {
        runTests();
    }

    public static void runTests() {
        test(0, 0);
        test(1, 1);
        test(2, 1);
        test(3, 2);
        test(4, 3);
        test(5, 5);
        test(6, 8);
        test(7, 13);
        test(10, 55);
        testNegative();
    }

    public static void test(int input, int expected) {
        try {
            int result = fibonacci(input);
            if (result == expected) {
                System.out.println("✅ Passed for input " + input);
            } else {
                System.out.println("❌ Failed for input " + input + ": expected " + expected + ", got " + result);
            }
        } catch (Exception e) {
            System.out.println("❌ Exception for input " + input + ": " + e.getMessage());
        }
    }

    public static void testNegative() {
        try {
            fibonacci(-1);
            System.out.println("❌ Failed: Expected exception for negative input");
        } catch (IllegalArgumentException e) {
            System.out.println("✅ Passed: Exception caught for negative input");
        } catch (Exception e) {
            System.out.println("❌ Failed: Unexpected exception for negative input: " + e.getMessage());
        }
    }
}
