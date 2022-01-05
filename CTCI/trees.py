# Binary tree implementation
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


def inOrder(node):
    if node is not None:
        inOrder(node.left)
        node.visit()
        inOrder(node.right)


def postOrder(node):
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        node.visit()


def preOrder(node):
    if node is not None:
        node.visit()
        preOrder(node.left)
        preOrder(node.right)


def main():
    print("Main function")


if __name__ == '__main__':
    main()
