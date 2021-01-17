class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        startSearch = word[0]
        startPoints = []
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == startSearch:
                    startPoints.append((i,j))
        print(startPoints)
        checkBoard = [[False]*len(board[0]) for _ in range(len(board))]
        print(checkBoard)
        for i in range(len(startPoints)):
            if self.backtrack(board, checkBoard, startPoints[i][0], startPoints[i][1], 0, word, moves):
                return True
            
    def backtrack(self, board, checkBoard, i, j, strLength, word, moves):
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
        if tempResult:        
            return tempResult
        checkBoard[i][j] = False
        return False
        
    def canMove(self, i, j, moves, checkBoard):
        if i + moves[0] > len(checkBoard) or i + moves[0] < 0 or j + moves[1] > len(checkBoard[0]) or j + moves[1] < 0:
            return False
        if checkBoard[i][j] == True:
            return False
        return True
        
        