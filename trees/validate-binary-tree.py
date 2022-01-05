"""
INPUT: Root of a tree
OUTPUT: Boolean representing whether tree is BST
"""

"""
Valid Binary Search tree criteria:
1. Nodes of left subtree have key less than root node key
2. Nodes of right subtree have key greater than root node key
3. Left and right subtrees must also be binary search trees (Obey rules 1 & 2)

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidUtil(node: TreeNode, lower=float("-inf"), upper=float("inf")):
            # Propagate recursion on base case (leaves)
            if not node:
                return True
            # Check if value within limits
            value = node.val
            if value >= upper or value <= lower:
                return False
            # Check left and right subtrees recursively
            if not isValidUtil(node.left, lower, value):
                return False
            if not isValidUtil(node.right, value, upper):
                return False

        return isValidUtil(root)


"""
Time complexity: 
Pre-order traversal used, which is a kind of depth first search. 
Therefore O(n+m)

Space complexity: 
Must have storage in stack for at most the entire contents of tree due to recursion
Therefore O(n)
Iterative version will have O(1) using stack and popping immediately with pre-order DFS
"""
