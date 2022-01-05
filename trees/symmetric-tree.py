# INPUT: Root node of a binary tree
# OUTPUT: True if tree symmetric, False otherwise

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def checkSymmetric(left: TreeNode, right: TreeNode) -> bool:
            if left and right and left.val == right.val:
                return checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)
            elif (left is None) and (right is None):
                return True
            else:
                return False

        return checkSymmetric(root.left, root.right)
