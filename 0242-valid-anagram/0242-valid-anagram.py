class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashset = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in hashset:
                hashset[i] += 1
            else:
                hashset[i] = 1
        for b in t:
            if b in hashset:
                hashset[b] -= 1
            else:
                return False
            
        for i in hashset:
            if hashset[i] != 0:
                return False
            
        return True