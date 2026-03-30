class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #s = s.replace(" ", "")
        s = "".join(ch for ch in s if ch.isalnum())
        reversal = "".join(reversed(s))
        if s == reversal:
            return True
        else:
            return False     