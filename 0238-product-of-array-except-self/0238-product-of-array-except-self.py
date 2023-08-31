class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
            
        print(result)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            print("i==>", result[i])
            result[i] = postfix * result[i]
            print("new result[i]",result[i])
            postfix *= nums[i]

            # [1,2,3,4] 1
            # [1,1,2,6]
            # [1,1,2,6]
            #   12 4 1
            # [x,8,8,6]
        print(result)
        return result
            