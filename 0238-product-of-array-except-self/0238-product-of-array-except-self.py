class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        # [1,2,3,4]
        # [1,1,2,6] 1 prefix
        # [x,24,12,4] 1 postfix
        # [24,12,8,6] result
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
        print(result)
        postfix = 1
        for y in range(len(nums)-1,-1,-1):
            result[y] = postfix * result[y]
            postfix *= nums[y]
        
        
        print(result)
        return result