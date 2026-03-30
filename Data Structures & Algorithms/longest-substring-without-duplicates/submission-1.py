class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        seen = set()
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        largest = 1

        for r in range(len(s)):
            if not s[r] in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            if len(seen) > largest:
                largest = len(seen)
        return largest