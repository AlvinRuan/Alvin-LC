class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        # input is a list
        # output is an array of distinct triplets that equal 0
        # exceptions: when given nums does not add up to 0 => return empty array
        
        collection = []

        nums.sort()
        
        for index,i in enumerate(nums):
            if index > 0 and i == nums[index-1]:
                continue
            left, right = index+1, len(nums)-1
            while left < right:
                threeSum = i + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left +=1
                else:
                    collection.append([i, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return collection