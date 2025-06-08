const assert = require('assert');

function fibonacci(n) {
    const sqrt5 = Math.sqrt(5);
    const phi = (1 + sqrt5) / 2;
    const psi = (1 - sqrt5) / 2;

    const fib = (Math.pow(phi, n) - Math.pow(psi, n)) / sqrt5;

    return Math.round(fib);  // Rounding to correct floating point errors
}


try {
    assert.strictEqual(fibonacci(0), 0);
    assert.strictEqual(fibonacci(1), 1);
    assert.strictEqual(fibonacci(2), 1);
    assert.strictEqual(fibonacci(3), 2);
    assert.strictEqual(fibonacci(4), 3);
    assert.strictEqual(fibonacci(5), 5);
    assert.strictEqual(fibonacci(10), 55);
    assert.strictEqual(fibonacci(20), 6765);

    console.log('✅ All test cases passed!');
} catch (err) {
    console.error('❌ Test failed:', err.message);
}
