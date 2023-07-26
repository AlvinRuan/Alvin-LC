class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        collection = set(nums)
        
        return len(collection) != len(nums)