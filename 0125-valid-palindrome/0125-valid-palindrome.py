class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        words = ""
        for i in s:
            if i.isalnum():
                words += i.lower()
        
        left = 0
        right = len(words)-1
        
        while left < right:
        
            if words[left] == words[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True