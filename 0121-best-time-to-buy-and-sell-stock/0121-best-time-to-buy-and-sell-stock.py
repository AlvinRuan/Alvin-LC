class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                current = prices[right] - prices[left]
                max_profit = max(max_profit, current)
            else:
                left = right
            
            right += 1
            

        
        return max_profit