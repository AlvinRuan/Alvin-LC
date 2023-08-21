class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
              
        if len(matrix) == None:
            return False
        
        
        target_matrix = None
        
        if len(matrix) == 1:
            target_matrix = matrix[0]
        
        top, bottom = 0, len(matrix)-1
        
        while top <= bottom:
            mid = (top+bottom)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                target_matrix = matrix[mid]
                break
                
        if target_matrix == None:
            return False
        
        left, right = 0, len(target_matrix)-1
        
        while left <= right:
            mid = (right+left)//2
            if target_matrix[mid] > target:
                right = mid - 1
            elif target_matrix[mid] < target:
                left = mid + 1
            else:
                return True
            
        return False
            
        
        
                
        