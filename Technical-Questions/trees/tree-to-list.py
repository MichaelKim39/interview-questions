# INPUT: Root of binary tree
# OUTPUT: Modify tree into flattened version such that it is identical to a linked list
# ASSUMPTIONS:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]
        prev = None
        while stack:
            current = stack.pop()
            if prev:
                prev.right = current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            current.left = None
            prev = current

# Runtime - Pre-order traversal with DFS so O(N)
# Space Complexity - Unbalanced O(N), Balanced (log(N))
