"""
CHECK BALANCED
Input: Binary tree
Output: Boolean based on whether the tree is balanced
Balanced: heights of the left and right subtree at any node never differ by more than one
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def visit(self, node):
        print(node.data)


class Tree:
    def __init__(self):
        self.root = None

# BRUTE FORCE
# Time complexity = O(nlogn)
# Space complexity =


def get_height(root: Node):
    if (root == null):
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


def brute_check_balanced(root: Node) -> bool:
    heightDiff = abs(get_height(root.left) - get_height(root.right))
    if heightDiff > 1:
        return False
    else:
        return brute_check_balanced(root.left) & brute_check_balanced(root.right)


def main():
    print("Main")


if __name__ == "__main__":
    main()
