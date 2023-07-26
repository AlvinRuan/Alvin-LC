class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        collection = set()
        
        for i in range(len(nums)):
            collection.add(nums[i])
        return len(collection) != len(nums)