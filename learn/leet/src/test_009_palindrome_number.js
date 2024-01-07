import { expect } from "chai";
import { describe, it } from "mocha";
function isPalindrome(x) {
    if (x < 0)
        return false;
    let stack = [];
    let current = x;
    while (current > 0) {
        stack.push(current % 10);
        current = Math.trunc(current / 10);
    }
    while (stack.length > 0) {
        const last = stack.pop();
        const first = stack[0];
        if (first === undefined) {
            return true;
        }
        if (last !== first) {
            return false;
        }
        stack = stack.slice(1, stack.length);
    }
    return true;
}
;
describe('test_009_palindrome_number', () => {
    it('should return true', () => {
        expect(isPalindrome(121)).to.be.true;
    });
});
//# sourceMappingURL=test_009_palindrome_number.js.map