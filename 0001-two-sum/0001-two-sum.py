class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collection = {}
        
        for i in range(len(nums)):
            
            result = target - nums[i]
            
            if nums[i] in collection:
                
                return [collection[nums[i]],i]
            
            else:
                collection[result] = i