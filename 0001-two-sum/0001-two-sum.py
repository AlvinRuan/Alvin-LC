class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        collection = {}

        for i in range(len(nums)):

            opposite = target - nums[i]

            if opposite in collection:
                return [i, collection[opposite]]

            else:
                collection[nums[i]] = i