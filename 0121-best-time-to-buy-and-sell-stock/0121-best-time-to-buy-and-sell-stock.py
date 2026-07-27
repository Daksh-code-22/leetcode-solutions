class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_prices = float("inf")

        for i in range(0, n):
            min_prices = min(min_prices, prices[i])
            max_profit = max(max_profit, prices[i]- min_prices)

        return max_profit
        