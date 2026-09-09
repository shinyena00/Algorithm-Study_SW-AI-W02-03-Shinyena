class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        size = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix) + 1):
            for j in range(len(matrix[0]) + 1):
                if i == 0 or j == 0:
                    continue
                if matrix[i-1][j-1] == "1":
                    if size[i][j-1] == size[i-1][j] == size[i-1][j-1] != 0:
                        size[i][j] = int((size[i][j-1] ** 0.5 + 1) ** 2)
                        if size[i][j] > result:
                            result = size[i][j]
                    else:
                        maximum =  max(size[i][j-1], size[i-1][j], size[i-1][j-1])
                        minimum = min(size[i][j-1], size[i-1][j], size[i-1][j-1])
                        if maximum > 0 and maximum - minimum <= 1 :
                            size[i][j] = maximum
                        else:
                            size[i][j] = int((minimum ** 0.5 + 1) ** 2)
                    if result == 0:
                        result += 1

        return result