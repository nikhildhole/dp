// brute_force/iteration.js
const assert = require('assert');

function fibonacci(n) {
    // You implement this
    if(n == 0){
        return 0
    } else if(n == 1){
        return 1
    } if(n == 2){
        return 1
    }
    temp = 0
    temp1 = 1
    temp2 = 1
    for(i = 2; i < n; i++){
        temp = temp1 + temp2
        temp2 = temp1
        temp1 = temp
    }

    return temp
}


// ✅ Test cases
try {
    assert.strictEqual(fibonacci(0), 0);
    assert.strictEqual(fibonacci(1), 1);
    assert.strictEqual(fibonacci(2), 1);
    assert.strictEqual(fibonacci(3), 2);
    assert.strictEqual(fibonacci(4), 3);
    assert.strictEqual(fibonacci(5), 5);
    assert.strictEqual(fibonacci(6), 8);
    assert.strictEqual(fibonacci(10), 55);
    assert.strictEqual(fibonacci(15), 610);
    assert.strictEqual(fibonacci(20), 6765);

    console.log('✅ All test cases passed!');
} catch (err) {
    console.error('❌ Test failed:', err.message);
}
