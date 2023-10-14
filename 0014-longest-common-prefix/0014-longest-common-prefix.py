class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        sorted_str = sorted(strs, key=len)
        
        shortest = sorted_str[0]
        
        for i in strs:
            while shortest != "":
                if i.startswith(shortest):
                    break
                else:
                    shortest = shortest[:-1]
                
                
        return shortest