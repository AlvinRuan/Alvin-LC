class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        midpoint = None
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        
        while left <= right:
            midpoint = (right+left)//2
            if nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
            else:
                return midpoint
            

        return -1