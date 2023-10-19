class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        collection = {}
        
        for i in nums:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
        print(collection)     
        sorted_collection = sorted(collection, key=lambda i:-collection[i])
        print(sorted_collection)
        
        return sorted_collection[:k]