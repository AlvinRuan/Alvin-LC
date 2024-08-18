class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        collection = {}

        for i in s:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1

        for j in t:
            if j in collection:
                collection[j] -= 1
            else:
                return False

        for i in collection:
            if collection[i] != 0:
                return False
        
        return True