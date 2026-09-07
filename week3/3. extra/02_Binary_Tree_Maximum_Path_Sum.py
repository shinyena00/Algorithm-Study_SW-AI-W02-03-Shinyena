# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maximum = float('-inf')

        
        def lookingfor(root: Optional[TreeNode]):
            nonlocal maximum

            if root == None:
                return 0

            left = max(0, lookingfor(root.left))

            right = max(0, lookingfor(root.right))

            temp = root.val + left + right
            if root.val + left + right > maximum:
                maximum = temp

            new = max(left, right)

            if maximum < root.val + new:
                maximum = root.val + new

            return root.val + new
        lookingfor(root)

        return maximum




        