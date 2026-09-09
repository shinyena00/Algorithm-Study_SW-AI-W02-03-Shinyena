class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 :
                    matrix[i][j] = j
                    continue
                if j == 0:
                    matrix[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
        return matrix[len(word1)][len(word2)]