class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isvalidunit(unit):
            digits = list(filter(lambda x: x.isdigit(), unit))
            return len(digits) == len(set(digits))

        for row in board:
            if not isvalidunit(row):
                return False

        for column_idx in range(9):
            column = [board[x][column_idx] for x in range(len(board))]
            if not isvalidunit(column):
                return False
        
        for row_hinge in range(0, 9, 3):
            for col_hinge in range(0, 9, 3):
                square = []
                for row_offset in range(3):
                    for offset in range(3):
                        square.append(board[row_hinge + row_offset][col_hinge + offset])
                if not isvalidunit(square):
                    return False
        
        return True

        

                





