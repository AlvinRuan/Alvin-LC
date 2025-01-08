class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]
        
        collection = {}
        for i in strs:
            alpha_order = ''.join(sorted(i))
            if alpha_order in collection:
        
                collection[alpha_order].append(i)
        
            else:
                collection[alpha_order] = [i]
        
        return list(collection.values())
        

        
        