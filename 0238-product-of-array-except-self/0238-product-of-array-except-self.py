class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        
        # I want to get the prefix product into the corresponding result location
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
        # do the same with suffix and multiply against the corresponding result location value
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        
        
        return result