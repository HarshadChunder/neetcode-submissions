class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, best_profit = 0, 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                best_profit  = max(best_profit, profit)

        return best_profit
            




        
        