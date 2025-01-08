class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1:
            return [strs]

        
        collection = {}
        
        for i in strs:
        
            print(i)
            alpha_order = ''.join(sorted(i))
            print(alpha_order)
        
            if alpha_order in collection:
        
                collection[alpha_order].append(i)
        
            else:
                collection[alpha_order] = [i]
            
        results = []
            
        for j in collection:
            results.append(collection[j])
        
        return results
        

        
        