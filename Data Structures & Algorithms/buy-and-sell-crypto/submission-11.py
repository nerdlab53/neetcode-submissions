class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        curr_min = prices[0]
        profit = 0
        for price in prices:
            curr_min = min(curr_min, price)
            profit = max(price-curr_min, profit)
        return profit