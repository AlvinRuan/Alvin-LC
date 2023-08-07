class Solution:
    def maxArea(self, height: List[int]) -> int:
        # oice
        
        # output = max amount of water it can contain
        # input = array of numbers
        # constraints
        # edge cases =  empty array
        
        
        result = 0
        
        left, right = 0, len(height)-1
        
        while left < right:
            if (min(height[left],height[right]) * (right-left)) > result:
                result = min(height[left],height[right]) * (right-left)
                
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                if height[left+1] > height[right-1]:
                        right -=1
                else:
                    left +=1
                
        return result
                