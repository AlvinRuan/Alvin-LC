class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        collection = {}

        for i in s:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
        
        for j in t:
            if j not in collection:
                return False
            else:
                collection[j] -= 1
        
        for k in collection:
            if collection[k] != 0:
                return False

        return True