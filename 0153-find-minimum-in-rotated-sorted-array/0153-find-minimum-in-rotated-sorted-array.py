class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right, lowest = 0, len(nums)-1, nums[0]
        
        
        
        while left <= right:
            if nums[left] < nums[right]:
                lowest = min(lowest,nums[left])
        
            
            mid = (right+left)//2
            lowest = min(nums[mid], lowest)
            if nums[mid] >= nums[left]:
                left = mid+1    
                
            else:
                right = mid-1
                
        return lowest