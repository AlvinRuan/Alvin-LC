class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # INPUT
        # OUTPUT
        # Constraints

        # create a dictionary, the purpose is to have each element counted as we go through the array
        collection = {}
        # as we loop through the array
        for i in nums:
        # if an integer doesn't exist in the dictionary, we create the first instance of it by doing
            if i in collection:
                collection[i]+= 1
            else:
                collection[i] = 1
        # dictionary[integer] = 1
        # else, we increment that dictionary[integer] count

        # after finishing,
        sorted_collection = sorted(collection, key=collection.get, reverse=True)

        return sorted_collection[0:k]

        # we sort the dictionary by the value of largest to smallest based on values, 
        # and then return the k amount of keys in an array

        
        