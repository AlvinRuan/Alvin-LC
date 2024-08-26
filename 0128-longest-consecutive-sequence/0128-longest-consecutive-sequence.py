class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_version = set(nums)

        longest = 0
        current_longest = 0

        for i in set_version:
            # check if its start of sequence
            if i-1 not in set_version:
                current_longest = 0
                while (i + current_longest ) in set_version:
                    current_longest += 1
                longest = max(longest, current_longest)

        return longest
            

