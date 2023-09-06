class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        collection = {}
        
        for index, i in enumerate(nums):
            result = target - i
            if result in collection:
                return [collection[result], index]
            collection[i] = index
            