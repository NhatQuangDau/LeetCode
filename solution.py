#main idea: check row, column and box to verify if a number is already existed

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = [[0 for i in range(10)] for j in range(9)]
        columnCheck = [[0 for i in range(10)] for j in range(9)]
        boxCheck = [[0 for i in range(10)] for j in range(9)]
        for row in range(9):
            for column in range(9):
                if board[row][column] != '.':
                    num = int(board[row][column])
                    if rowCheck[row][num] == 1 or columnCheck[column][num] == 1 or boxCheck[row//3 * 3 + column//3][num] == 1:
                        return False
                    rowCheck[row][num] = 1
                    columnCheck[column][num] = 1
                    boxCheck[row//3 * 3 + column//3][num] = 1
        return True
