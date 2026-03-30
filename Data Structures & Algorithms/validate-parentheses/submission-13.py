from collections import Counter
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1 or s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False

        stk = []
        for i in range(len(s)):
            if s[i] == ")":
                if not stk:
                    return False
                if not stk.pop() == "(":
                    return False
            elif s[i] == "]":
                if not stk:
                    return False
                if not stk.pop() == "[":
                    return False
            elif s[i] == "}":
                if not stk:
                    return False
                if not stk.pop() == "{":
                    return False
            else:
                stk.append(s[i])
        return not stk
        