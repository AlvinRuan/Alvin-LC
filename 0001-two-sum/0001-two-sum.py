class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        collection = {}

        for i in range(len(nums)):
            other_half = target - nums[i] 
            if other_half in collection:
                return [i, collection[other_half]]
            else:
                collection[nums[i]] = i
