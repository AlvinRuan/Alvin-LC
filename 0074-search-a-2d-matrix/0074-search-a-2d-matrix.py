class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        
        if len(matrix) == None:
            return False
        
        target_matrix = None
        for i in matrix:
            if (target in i):
                target_matrix = i
                
        if target_matrix == None:
            return False
        
        left, right = 0, len(target_matrix)
        
        while left <= right:
            mid = (right+left)//2
            if target_matrix[mid] > target:
                right = mid - 1
            elif target_matrix[mid] < target:
                left = mid + 1
            else:
                return True
            
        return False
            
        
        
                
        