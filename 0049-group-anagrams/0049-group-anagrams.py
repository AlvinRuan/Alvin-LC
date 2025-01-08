class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Input = an array of strings
        # Output = an array of arrays
        # Contraints
        # 

        # if strs.length === 1:
        # return strs
        # start a dictionary to collect as we loop
        # as we loop through this
        # rearrange the existing increment into alphanumeric order
        # check if it exists in the dictionary
        # if it does, we push onto the array, the un-alphanumeric ordered string
        # if it does not, we create the key value pair with they key being the alpa-numeric'd string
        # and the value being [ the incremented item ]

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
            
        # results = []
            
        # for j in collection:
        #     results.append(collection[j])
        
        return list(collection.values())
        

        
        