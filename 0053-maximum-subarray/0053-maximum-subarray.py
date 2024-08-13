class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        currentMax = nums[0]

        for n in nums:
            if currentSum < 0:
                currentSum = 0
            
            currentSum += n
            currentMax = max(currentMax, currentSum)

        return currentMax