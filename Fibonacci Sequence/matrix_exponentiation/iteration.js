const assert = require('assert');

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
