# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.BalanceValidator(root) != -1
    
    def BalanceValidator(self, node: Optional[TreeNode]) -> int: # Evaluates heights
        if not node:
            return 0

        leftHeight = self.BalanceValidator(node.left)
        rightHeight = self.BalanceValidator(node.right)

        if (leftHeight == -1 or rightHeight == -1):
            return -1 

        if abs(leftHeight - rightHeight) > 1:
            return -1 

        return 1 + max(leftHeight, rightHeight)