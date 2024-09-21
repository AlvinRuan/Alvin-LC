class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        # print(numbers[left])
        # print(numbers[right])
        # sum_lr = numbers[left] + numbers[right]
        # print(sum_lr)

        while right > left:
            sum_lr = numbers[left] + numbers[right]
            if sum_lr == target:
                return [left+1,right+1]
            elif sum_lr > target:
                right -= 1
            else:
                left += 1
        



        