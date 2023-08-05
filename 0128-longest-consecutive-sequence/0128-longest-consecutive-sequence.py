class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0
        collection = []
        
        for i in numSet:
            if (i-1) not in numSet:
                collection.append(i)
                longest = 1
        
        for i in collection:
            current_longest = 1
            while (i+1) in numSet:
                current_longest += 1
                i +=1
            if current_longest > longest:
                longest = current_longest
        
        return longest
            
                
        
        