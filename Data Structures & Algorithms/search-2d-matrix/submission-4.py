class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchColumn(matrix, target):
            
            
            n = len(matrix[0]) - 1

            for colidx in range(len(matrix)):
                lower = matrix[colidx][0]
                upper = matrix[colidx][n]
                if target >= lower and target <= upper:
                    return colidx
            return 0

        def bs(matrix, target, colidx):
            row = matrix[colidx]
            start, end = 0, len(row) - 1

            while start <= end:
                mid = start + ((end - start) // 2)
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return False

        return bs(matrix, target, searchColumn(matrix, target))
                