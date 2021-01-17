moves = [[1,0],[-1,0],[0,1],[0,-1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        startSearch = word[0]
        startPoints = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == startSearch:
                    startPoints.append((i,j))
        print(startPoints)
        checkBoard = [[False]*len(board[0]) for _ in range(len(board))]
        print(checkBoard)
        for point in startPoints:
            if self.backtrack(board, checkBoard, point[0], point[1], 0, word):
                return True
        
        return False
            
    def backtrack(self, board, checkBoard, i, j, strLength, word):
        if strLength == len(word):
            return True
        if board[i][j] != word[strLength]:
            return False
        
        checkBoard[i][j] = True
        print(board[i][j])
        tempResult = False
        for h in range(len(moves)):
            if self.canMove(i, j, moves[h], checkBoard):
                tempResult = tempResult or self.backtrack(board, checkBoard, i + moves[h][0], j + moves[h][1], strLength + 1, word)    
        checkBoard[i][j] = False
        return tempResult
        
    def canMove(self, i, j, move, checkBoard):
        if i + move[0] >= len(checkBoard) or i + move[0] < 0 or j + move[1] >= len(checkBoard[0]) or j + move[1] < 0:
            return False
        if checkBoard[i][j] == True:
            return False
        return True
        
        