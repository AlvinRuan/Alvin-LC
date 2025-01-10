class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        collection = {}
        
        for i in nums:
        
            if i in collection:
                collection[i]+= 1
            else:
                collection[i] = 1
        
        sorted_collection = sorted(collection, key=lambda x:-collection[x])

        return sorted_collection[0:k]

        

        
        