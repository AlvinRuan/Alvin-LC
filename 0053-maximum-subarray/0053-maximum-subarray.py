class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currentMax = nums[0]
        currentArrayTotal = 0


        for n in nums:
            if currentArrayTotal < 0:
                currentArrayTotal = 0

            currentArrayTotal += n
            currentMax = max(currentMax, currentArrayTotal)

        return currentMax