from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        count = Counter(nums)

        return [num for num, freq in count.most_common(k)]