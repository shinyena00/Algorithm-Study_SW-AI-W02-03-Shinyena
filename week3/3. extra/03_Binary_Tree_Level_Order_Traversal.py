

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        step = 1
        temp = [root]

        result = []
        level = []

        while(True):
            result.append([node.val for node in temp])
            for i in temp:
                if i.left is not None:
                    level.append(i.left)
                if i.right is not None:
                    level.append(i.right)
            if not level:
                break
            temp = level[:]
            level.clear()
        
        return result
            

        