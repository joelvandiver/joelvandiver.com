class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue
            
            if not stack:
                return False
            
            last = stack.pop()

            if c == ')':
                if last == "(":
                    continue

            if c == ']':
                if last == "[":
                    continue
                    
            if c == '}':
                if last == "{":
                    continue
            return False
        if stack:
            return False
        return True


def test_1():
    assert Solution().isValid("()")

def test_2():
    assert not Solution().isValid("(]")
