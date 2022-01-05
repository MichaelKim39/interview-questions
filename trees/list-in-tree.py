"""
QUESTION: 
Given a binary tree root and a linked list with head as the first node.
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.
"""

# INPUT: Linked List Head, Binary Tree Root
# OUTPUT: True if linked list appears as downward path in tree, False otherwise

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Convert linked list to array
        listAsArray = []
        current = head
        while current:
            listAsArray.append(current.val)
            current = current.next
        # Function to check contiguous subarray

        def isSubArray(subArray, array):
            i = 0
            j = 0
            while i < len(array) and j < len(subArray):
                if array[i] == array[j]:
                    i += 1
                    j += 1
                    if j == len(subArray):
                        return True
                else:
                    # Increment i and reset j
                    i = i - j + 1
                    j = 0
        # Function to check paths in DFS fashion

        def checkPath(node, path):
            path.append(node.val)
            # check listAsArray is subsequence somehow
            if isSubArray(listAsArray, path):
                return True
            if node.left:
                checkPath(node.left, path)
            if node.right:
                checkPath(node.right, path)

        # Run DFS on tree
        checkPath(root, [])
        return False

# ---------------------------------------------------------------------------- #
#                                BRUTE FORCE DFS                               #
# ---------------------------------------------------------------------------- #

# Works by checking for each subpath whether the link fits
    def isSubPath(self, head, root):
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return head.val == root.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# Time Complexity - O(N * min(L * H))
# Space Complexity - O(H)

# ---------------------------------------------------------------------------- #
#                              DYNAMIC PROGRAMMING                             #
# ---------------------------------------------------------------------------- #

# Uses knuth morris pratt algorithm
    def isSubPath(self, head, root):
        pattern = [head.val]
        indices = [0]
        node = head.next

        # Constructing LPS table
        i = 0
        while node:
            while i and node.val != pattern[i]:
                i = indices[i-1]
            if node.val == pattern[i]:
                i += 1
            pattern.append(node.val)
            indices.append(i)
            node = node.next

        # Recursively run KMP-DFS variant
        def dfs(root, i):
            if not root:
                return False
            while i and root.val != pattern[i]:
                i = indices[i-1]
            if root.val == pattern[i]:
                i += 1
            return i == len(indices) or dfs(root.left, i) or dfs(root.right, i)

        # First call
        return dfs(root, 0)

# Time complexity: O(N) because touches each node once (just dfs and generating lps is linear too)
# Space complexity: O(L + H) because recursive call stack for lps is at most L and for dfs recursion is at most H
