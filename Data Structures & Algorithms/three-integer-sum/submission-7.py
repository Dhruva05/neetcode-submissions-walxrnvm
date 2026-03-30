class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums = sorted(nums)
        i = 0
        while i < (len(nums) - 2):
            if not ((nums[i] == nums[i-1]) and (i > 0)):
                k = len(nums) - 1
                j = i + 1
                while j < k:
                    sum = nums[j] + nums[k]
                    if (sum + nums[i]) == 0:
                        final.append([nums[i], nums[j], nums[k]])
                        k -= 1
                        j +=1
                        while j < k and nums[k+1] == nums[k]:
                            k -= 1
                        while j < k and nums[j-1] == nums[j]:
                            j +=1
                    elif sum > -nums[i]:
                        k -= 1
                    elif sum < -nums[i]:
                        j += 1
            i += 1
        return final