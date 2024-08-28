class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_version = set(nums)

        longest = 0
        current_longest = 0

        for i in nums:
            if i-1 not in set_version:
                current_longest = 1
                while i+1 in set_version:
                    current_longest += 1
                    i+= 1
                longest = max(current_longest, longest)
        
        return longest
            

