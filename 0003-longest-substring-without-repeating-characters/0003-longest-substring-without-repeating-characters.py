class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        
        longest_substring = 0

        left =  0
        right = 1
        current_string = s[left]

        while right < len(s):
            
            if s[right] in current_string:
                while s[right] in current_string and left <= right:
                    left += 1
                    current_string = s[left:right]
                current_string += s[right]
            else:
                current_string += s[right]
                
            longest_substring = max(len(current_string), longest_substring)
            right += 1

        return longest_substring