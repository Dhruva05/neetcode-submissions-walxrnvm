class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        List = []
        for i in range(len(nums)):
            if nums[i] in List:
                return True
            List.append(nums[i])
        return False
