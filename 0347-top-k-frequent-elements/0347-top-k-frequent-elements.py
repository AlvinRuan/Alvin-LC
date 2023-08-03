class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        # initial a collection / hashmap
        
        collection = {}
        
        # loop through the array of numbers
        
        for i in nums:
        # if number, doesn't exist, hashmap[number] = 1
        
            if i in collection:
                collection[i] += 1
            else:
                collection[i] = 1
        # else hashmap[number] += 1
        
        # loop through hashmap, and append numbers to empty array = result
        
        result = []
        
        for i in collection:
        # reverse sort array
            result.append([collection[i], i])
        # largest_to_smallest = sorted(result,key=,reverse=True)
        largest_to_smallest = sorted(result, reverse=True)

        # another for loop decrementing the value of K
        
        # appending each one to the result array
        
        resulting = []
        
        for i in range(k):
            resulting.append(largest_to_smallest[i][1])
            
        return resulting