class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        collection = {}
        
        # Add to collection
        for i in s:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
                
        for i in t:
            if i in collection:
                collection[i] -= 1
            else:
                return i
            
        for i in collection:
            if collection[i] == -1:
                return i
            