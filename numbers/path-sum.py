# INPUT: root node of binary tree, integer sum
# OUTPUT: True if there exists root-leaf path whose node values sum to exact value of input

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [root]

        while stack:
            current = stack.pop()

            if current.right:
                current.right.val += current.val
                stack.append(current.right)
            if current.left:
                current.left.val += current.val
                stack.append(current.left)
            if (not current.left) and (not current.right):
                if current.val == sum:
                    return True

        return False

# Runtime - O(#nodes)
# Space complexity - O(height)
