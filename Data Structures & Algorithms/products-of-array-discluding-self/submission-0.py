class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        final = []
        prod_left = 1
        prod_right = 1
        for i in range(len(nums)):
            left.append(prod_left)
            prod_left *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            right.append(prod_right)
            prod_right *= nums[i]
        right.reverse()

        for i in range(len(nums)):
            index = (left[i]) * (right[i])
            final.append(index)

        return final




