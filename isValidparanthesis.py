class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            if ch in pairs:  # opening bracket
                stk.append(ch)
            else:  # closing bracket
                if not stk: 
                    return False
                if pairs[stk[-1]] != ch:
                    return False
                stk.pop()

        return len(stk) == 0
