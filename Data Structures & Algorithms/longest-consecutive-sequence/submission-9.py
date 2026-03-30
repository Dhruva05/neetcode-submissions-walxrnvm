class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        largest = []
        counter = 1
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        for x in s:
            if (x - 1) not in s:
                curr = x
                while (curr + 1) in s:
                    counter += 1
                    curr += 1
                largest.append(counter)
                counter = 1
        return max(largest)