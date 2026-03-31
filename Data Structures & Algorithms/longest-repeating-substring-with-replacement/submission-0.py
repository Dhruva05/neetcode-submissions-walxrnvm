class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        max_count = 0
        largest = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_count = max(max_count, hashmap[s[r]])
            window_size = r - l + 1

            if window_size - max_count > k:
                hashmap[s[l]] -= 1
                l += 1

            largest = max(largest, r - l + 1)
        return largest