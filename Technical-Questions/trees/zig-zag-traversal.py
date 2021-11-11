# INPUT: root of binary tree
# OUTPUT: Zig zag level order traversal of node values (in nested array format)
# INFORMATION:
#   Read first lavel left-to-right, next right-to-left and alternate
#   Return each level in the correct order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # Initiate
        current_level = [root]
        next_level = []
        overall_result = []
        level_result = []
        depth = 0

        while current_level:
            node = current_level.pop()
            level_result.append(node.val)
            children = [child for child in [node.left, node.right] if child]
            # If even enforce regular order
            if depth % 2 == 0:
                next_level += children
            # Otherwise enforce reverse order
            else:
                next_level += children[::-1]
            # If no nodes remain in current level, reset
            if not current_level:
                current_level = next_level
                next_level = []
                overall_result.append(level_result)
                level_result = []
                depth += 1

        return overall_result
