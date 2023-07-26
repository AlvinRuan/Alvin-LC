class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        collection = {}

        for i in range(len(nums)):
            result = target - nums[i]
            if result in collection:
                return [i, collection[result]]
            else:
                collection[nums[i]] = i