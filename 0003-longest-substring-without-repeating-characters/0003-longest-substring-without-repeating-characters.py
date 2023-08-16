class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left,longest = 0,0
        
        collection = set()
        
        for right in range(len(s)):
            while s[right] in collection:
                collection.remove(s[left])
                left += 1
            collection.add(s[right])
            
            longest = max(longest, right - left + 1)
            
        return longest
            