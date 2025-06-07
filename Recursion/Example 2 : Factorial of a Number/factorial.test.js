const factorial = require('./factorial');

describe('Factorial Function (Recursive)', () => {
    test('Factorial of 0 should be 1', () => {
        expect(factorial(0)).toBe(1);
    });

    test('Factorial of 1 should be 1', () => {
        expect(factorial(1)).toBe(1);
    });

    test('Factorial of 3 should be 6', () => {
        expect(factorial(3)).toBe(6);
    });

    test('Factorial of 5 should be 120', () => {
        expect(factorial(5)).toBe(120);
    });

    test('Factorial of 10 should be 3628800', () => {
        expect(factorial(10)).toBe(3628800);
    });

    test('Throws error on negative input', () => {
        expect(() => factorial(-1)).toThrow(Error);
    });

    test('Throws error on non-integer input', () => {
        expect(() => factorial(3.5)).toThrow(Error);
    });
});
