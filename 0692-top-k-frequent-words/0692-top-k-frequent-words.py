class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        collection = {}
        
        for i in words:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
        
        sorted_collection = sorted(collection, key= lambda x:(-collection[x],x))
            
        return sorted_collection[:k]
        