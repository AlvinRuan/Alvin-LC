class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        collection = {}

        for i in nums:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
        
        sort_collection = sorted(collection, key=lambda x:-collection[x])
        return sort_collection[0:k]
        