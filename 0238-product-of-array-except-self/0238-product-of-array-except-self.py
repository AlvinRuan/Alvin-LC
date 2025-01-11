class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Input = an array
        # Output = array of products
        # Contraints = cannot use division & must be O(n)
        # Edge Case = when there's 0s, the result is zero

        prefix = []

        # as we loop through the nums,
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        prefix_accum = 1
        for i in range(len(nums)):
            prefix.append(prefix_accum)
            prefix_accum *= nums[i]
        

        postfix_accum = 1
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [24, 12, 8, 6]
        for j in range(len(nums)-1,-1,-1):
            prefix[j] *= postfix_accum
            postfix_accum *= nums[j]
            
        return prefix
