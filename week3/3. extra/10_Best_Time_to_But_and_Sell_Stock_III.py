#최적화 한 버전

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        if len(prices) ==2:
            return max(0, prices[1]- prices[0])
        if len(prices) == 3:
            return max(0, prices[1]- prices[0], prices[2]- prices[0], prices[2]- prices[1])

        buy1 = - prices[0]
        sell1 = float('-inf')
        buy2 = float('-inf')
        sell2 = float('-inf')

        for i in range(len(prices)):
            if -prices[i] > buy1:
                buy1  = -prices[i]
            if i == 0:
                continue
            if sell1 < prices[i] + buy1:
                sell1 = prices[i] + buy1
            if i == 1:
                continue
            if buy2 < sell1 - prices[i]:
                buy2 = sell1 - prices[i]
            if i== 2:
                continue
            if sell2 < buy2 + prices[i]:
                sell2 = buy2 + prices[i]
        
        return sell2



# 처음 짠 버전


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        if len(prices) ==2:
            return max(0, prices[1]- prices[0])
        if len(prices) == 3:
            return max(0, prices[1]- prices[0], prices[2]- prices[0], prices[2]- prices[1])
            
        matrix = [[float('-inf')] *5 for _ in range(len(prices))]

        for i in range(len(prices)):
            for j in range(5):
                if (i == 0 and j>=2) or (i == 1 and j >=3) or (i==2 and j==4):
                    continue
                if j == 0:
                    matrix[i][j] = 0
                    continue
                if i == 0 and j == 1:
                    matrix[i][j] = -prices[i]t
                if j % 2 == 0:
                    if matrix[i][j-1] + prices[i] > matrix[i-1][j]:
                        matrix[i][j]= matrix[i][j-1] + prices[i]
                    else:
                        matrix[i][j] = matrix[i-1][j]
                    continue
                if matrix[i-1][j] > matrix[i][j-1] - prices[i]:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i][j-1] - prices[i]
        return matrix[len(prices)-1][4]