class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        shortest = min(strs, key=len)

        for i in strs:
            while shortest !=  "":
                if i.startswith(shortest):
                    break
                else:
                    shortest = shortest[:-1]
                
        return shortest