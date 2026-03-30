class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        sell = 0
        if len(prices) == 1:
            return 0
        lowest = prices[0]
        highest = prices[1]
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                temp = prices[r] - prices[l]
                if temp > sell:
                    sell = temp
            elif prices[r] < lowest:
                lowest = prices[r]
                l = r
        return sell