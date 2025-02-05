class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Input = Array
        # Output = array of arrays that contain the sum of elements which = 0
        # Constraints = i !=j, i !=k, j != k 

        result = []

        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            left = i + 1 
            right = len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left] ,nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1 ] and left < right:
                        left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return result


