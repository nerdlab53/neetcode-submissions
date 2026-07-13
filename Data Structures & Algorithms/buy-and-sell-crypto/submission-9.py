class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices) - 1
        curr_min = prices[0]
        left_min = 0
        right_max = n
        profit = 0
        for i in range(n):
            if prices[i] <= curr_min:
                curr_min = prices[i]
            j = i + 1
            while j <= n:
                if prices[j] > curr_min:
                    profit = max(prices[j] - curr_min, profit)
                else:
                    j += 1    
                j += 1
        return profit