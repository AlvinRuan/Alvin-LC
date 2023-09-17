class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        greatest = max(nums)
        smallest = min(nums)
        for i in range(smallest,0,-1):
            if smallest%i == 0 and greatest %i == 0:
                return i
            
        
        
        