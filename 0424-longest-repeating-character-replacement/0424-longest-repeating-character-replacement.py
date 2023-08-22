class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        collection = {}
        
        left, right, longest = 0,0,0
        maxf = 0
        # parse through the string, we add to the set, as long as the amount is not greater than k's value

        while right < len(s):
            
            if s[right] in collection:
                collection[s[right]] += 1
            else:
                collection[s[right]] = 1
            
            maxf = max(maxf, collection[s[right]])
            while right - left + 1 - maxf > k:
                collection[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)
            right += 1
            
        return longest