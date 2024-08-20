class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        prefix = 1
        for i in nums:
            result.append(prefix)
            prefix *= i

        postfix = 1

        for j in range(len(nums)-1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
            

        return result