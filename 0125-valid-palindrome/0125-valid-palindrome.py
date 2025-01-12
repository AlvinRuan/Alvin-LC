class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # add all a-z characters into a string
        words = ""
        for i in s:
            if i.isalnum():
                words += i.lower()
        # left and right pointer
        left = 0
        right = len(words)-1
        # while right > left
        while left < right:
        # check left & right pointer
            if words[left] == words[right]:
                left += 1
                right -= 1
            else:
                return False
        # if equal, increment left, decrement right, continue loop
        # else return false
        # return false if successfully finished while loop
        return True