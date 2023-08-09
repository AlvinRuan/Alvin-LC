class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        highest = 0

        
        while right < len(prices):
            if prices[right] > prices[left]:
                if highest < prices[right] - prices[left]:
                    highest = prices[right] - prices[left]
            else:
                left = right
                
            right += 1
            
        return highest