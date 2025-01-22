class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ""

        for i in s:
            if i.isalnum():
                word += i.lower()

        l = 0
        r = len(word)-1

        while r > l:
            if word[r] != word[l]:
                return False
            l += 1
            r -= 1
        
        return True
            