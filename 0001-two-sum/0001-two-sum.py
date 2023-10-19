class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        collection =  {}
        
        for i in range(0, len(nums)):
            current = target - nums[i]
            if current in collection:
                return [collection[current], i]
            else:
                collection[nums[i]] = i
        
            