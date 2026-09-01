"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid[0])
        if n == 1:
            target = grid[0][0]
            return Node(target, 1, None, None, None, None)

        mid = n//2

        flag = True
        target = grid[0][0]
        for i in range(n):
            if sum(grid[i]) != target*n:
                flag = False
                break
        if flag:
            return Node(target, 1, None,None,None,None)


        top_left = [row[:mid] for row in grid[:mid]]
        top_right = [row[mid:] for row in grid[:mid]]
        bottom_left = [row[:mid] for row in grid[mid:]]
        bottom_right = [row[mid:] for row in grid[mid:]]



        top_left_temp = self.construct(top_left)
        
        top_right_temp = self.construct(top_right)

        bottom_left_temp = self.construct(bottom_left)

        bottom_right_temp = self.construct(bottom_right)

            

        return Node(1, 0, top_left_temp, top_right_temp, bottom_left_temp,bottom_right_temp)




        

        

        
        