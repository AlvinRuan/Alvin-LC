class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        collection = {}

        for i in nums:
            if i in collection:
                return True
            else:
                collection[i] = 1
        
        return False