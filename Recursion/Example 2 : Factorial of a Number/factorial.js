const { throws } = require("assert");

/**
 * Calculates the factorial of a non-negative integer using recursion.
 *
 * A factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
 * - 0! is defined as 1
 * - Factorial is only defined for non-negative integers
 *
 * @param {number} n - A non-negative integer
 * @returns {number} The factorial of the input number
 *
 * @throws {Error} If n is negative or not an integer
 */
function factorial(n) {
    // TODO: Implement this function using recursion
    if(n < 0){
        throw new Error(n + "should be positive");
    }
    if(!(typeof n === "number" && n % 1 === 0)){
        throw new Error(n + "should be integer");
    }

    if(n <= 1){
        return 1;
    }

    return factorial(n - 1) * n;
}

module.exports = factorial;