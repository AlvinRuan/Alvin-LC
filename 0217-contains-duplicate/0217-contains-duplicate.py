class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        set_version = set(nums)

        return len(set_version) != len(nums)