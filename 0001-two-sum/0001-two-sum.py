class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        collection = {}

        for i in range(len(nums)):
            other_half = target - nums[i] #  other_half(7) = 9 - i(2)
                                          #  other_half(2) = 9 - i(7)
            # if we find 7, we want to pair that index with index of i
            # else, we add the pair and index into the collection
            if other_half in collection:
                return [i, collection[other_half]]
            else:
                collection[nums[i]] = i # {2 : 0}
