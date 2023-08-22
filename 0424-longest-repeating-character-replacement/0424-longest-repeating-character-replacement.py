class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        collection = {}
        
        left, right, longest = 0,0,0
        
        # parse through the string, we add to the set, as long as the amount is not greater than k's value

        while right < len(s):
            
            if s[right] in collection:
                collection[s[right]] += 1
            else:
                collection[s[right]] = 1
                
            most_common = max(collection.values())
            check = right - left + 1 - most_common
            while check > k:
                collection[s[left]] -= 1
                left += 1
                most_common = max(collection.values())
                check = right - left + 1 - most_common
            longest = max(longest, right-left+1)
            right += 1
        return longest