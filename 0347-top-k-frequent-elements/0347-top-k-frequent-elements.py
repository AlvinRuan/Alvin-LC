class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        # initial a collection / hashmap
        
        if len(nums) == 1:
            return [nums[0]]
        
        collection = {}
        for i in nums:
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
                
        
        flipped = []
        for i in collection:
            flipped.append([collection[i],i])
        
        # sort array
        sorted_array = sorted(flipped, reverse=True)
        result = []
        
        for i in range(k):
            result.append(sorted_array[i][1])
        
        return result