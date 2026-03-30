class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0

        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            maximum = max(maximum, (price - lowest))

        return maximum