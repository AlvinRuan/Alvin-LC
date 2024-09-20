class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_Str = ""

        for i in s:
            if i.isalnum():
                new_Str += i.lower()

        return new_Str == new_Str[::-1]