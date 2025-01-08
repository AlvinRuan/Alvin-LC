class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Input = an array of strings
        # Output = an array of arrays
        # Contraints
        # 

        # if strs.length === 1:
        # return strs
        if len(strs) == 1:
            return [strs]

        # start a dictionary to collect as we loop
        collection = {}
        # as we loop through this
        for i in strs:
        # rearrange the existing increment into alphanumeric order
            print(i)
            alpha_order = ''.join(sorted(i))
            print(alpha_order)
        # check if it exists in the dictionary
            if alpha_order in collection:
        # if it does, we push onto the array, the un-alphanumeric ordered string
                collection[alpha_order].append(i)
        # if it does not, we create the key value pair with they key being the alpa-numeric'd string
            else:
                collection[alpha_order] = [i]
            # and the value being [ the incremented item ]
        results = []
        
        for j in collection:
            results.append(collection[j])
        
        return results
        

        
        