class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        collection =  set(nums)
        max_length = 0

        # for i in nums:
        #     if i in collection:
        #         continue
        #     else:
        #         collection[i] = 1
        
        # sorted_collection = sorted(collection, key=lambda x:x)

        

        for i in collection:

            if i-1 not in collection:
                current = i
                current_length = 1
                while (i+1) in collection:
                    current_length += 1
                    i += 1
                max_length = max(current_length, max_length)

        return max_length
        