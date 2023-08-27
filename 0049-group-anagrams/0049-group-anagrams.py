class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        collection = {}
        
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in collection:
                collection[sorted_i].append(i)
            else:
                collection[sorted_i] = [i]
        
        
        result = []
        for i in collection:
            result.append(collection[i])
        return result