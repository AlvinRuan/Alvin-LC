class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        greatest = max(nums)
        smallest = min(nums)
        print(greatest)
        print(smallest)
        for i in range(smallest, 0, -1):
            
            if greatest % i == 0 and smallest % i == 0:
                print(i)
                return i
        
        
        