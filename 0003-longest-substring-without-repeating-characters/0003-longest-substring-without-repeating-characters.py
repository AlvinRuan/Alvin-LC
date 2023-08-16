class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right, longest = 0,0,0
        
        collection = set()
        
        while right < len(s):
            while s[right] in collection:
                collection.remove(s[left])
                left += 1
            collection.add(s[right])
            
            longest = max(longest, right - left + 1)
            right += 1
        return longest
            