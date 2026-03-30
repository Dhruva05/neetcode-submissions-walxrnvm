class Solution:
    def maxArea(self, heights: List[int]) -> int:
        larg_area = 0
        for i in range(len(heights)):
            for y in range(i+1, len(heights)):
                height = min(heights[i], heights[y])
                length = y - i
                sum = height*length
                if sum > larg_area:
                    larg_area = sum
        return larg_area

        