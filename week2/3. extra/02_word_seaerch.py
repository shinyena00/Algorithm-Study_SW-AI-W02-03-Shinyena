class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()

        
        def word_search(row, col):
            path.add((row, col))

            if (len(path) == len(word)):
                return True

            word_index = len(path)
            result = False
            if row > 0:
                if (board[row-1][col] == word[word_index]) and ((row-1,col) not in path):
                    result = word_search(row-1,col)
            if col > 0:
                if (board[row][col-1] == word[word_index]) and ((row,col-1) not in path):
                    if not result:
                        result = word_search(row,col-1)
            if row < m -1:
                if (board[row+1][col] == word[word_index]) and ((row + 1,col) not in path):
                    if not result:
                        result = word_search(row+1,col)
            if col < n - 1:
                if (board[row][col+1] == word[word_index]) and ((row,col+1) not in path):
                    if not result:
                        result = word_search(row,col+1)

            if result == True:
                return True
            path.remove((row, col))

            return False  

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    result = word_search(i, j)
                    if result == True:
                        return True
        return False



