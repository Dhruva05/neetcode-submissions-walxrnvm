class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = nums[0]
        for i in range(len(nums)):
            if nums[i] < lowest:
                lowest = nums[i]
        return lowest
        