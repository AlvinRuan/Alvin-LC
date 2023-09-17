class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        result = 0
        nums.sort()
        
        for i in range(len(nums) -2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if target > total:
                    result += right - left
                    left += 1
                else:
                    right -= 1
            
        return result
                    
        