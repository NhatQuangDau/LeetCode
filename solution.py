#main idea: check row, column and box to verify if a number is already existed

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue
                if not self.validate(board, row, column):
                    return False
        return True
    
    def validate(self, board, row, column) -> bool:
        for i in range(row + 1, 9):
            if board[row][column] == board[i][column]:
                return False
        for i in range(column + 1, 9):
            if board[row][column] == board[row][i]:
                return False
        for i in range((row % 3) * 3 + column % 3 + 1, 9):
            if board[row][column] == board[row//3 * 3 + i//3][column//3 * 3 + i % 3]:
                return False
        return True
