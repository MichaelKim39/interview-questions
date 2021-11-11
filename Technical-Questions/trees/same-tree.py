from collections import deque

# INPUT: Root nodes of two binary trees
# OUTPUT: True if binary trees are equal, false otherwise
# ASSUMPTIONS:
# Binary trees are identical if they have same structure and nodes have same value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both empty considered equal / deals with base case
        if not p and not q:
            return True
        # Only one empty considered not equal
        if bool(p) != bool(q):
            return False
        # If not same value considered not equal
        if p.val != q.val:
            return False
        # Apply recursion
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

# Runtime: O(N) - visits each node exactly once
# Space Complexity: Balanced tree O(log(N)), Unbalanced tree O(N) - due to recursion stack

    def isSameTreeIter(self, p: TreeNode, q: TreeNode) -> bool:

        def checkSame(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if bool(p) != bool(q):
                return False
            if p.val != q.val:
                return False

        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if checkSame(p, q):
                queue.append(p.left, q.left)
                queue.append(p.right, q.right)
            else:
                return False
        return True

# Runtime - Still O(N)
# Space Complexity - Still O(log(N))
