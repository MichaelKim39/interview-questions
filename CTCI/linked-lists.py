class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join([str(node) for node in nodes])

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def remove_node(self, node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == node_data:
            self.head = head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Node not found")


# test linked list structure
def fill_llist(llist):
    first_node = Node('first')
    second_node = Node('second')
    third_node = Node('third')
    first_node.next = second_node
    second_node.next = third_node
    llist.head = first_node
    llist.add_last(Node('fourth'))
    llist.add_last(Node('fourth'))
    llist.add_last(Node('fifth'))
    llist.add_last(Node('fourth'))
    llist.remove_node('third')
    print("List: ", llist)


def fill_llist_nums(llist):
    first_node = Node(6)
    second_node = Node(2)
    third_node = Node(1)
    first_node.next = second_node
    second_node.next = third_node
    llist.head = first_node
    llist.add_last(Node(9))
    llist.add_last(Node(4))
    llist.add_last(Node(3))
    llist.add_last(Node(4))
    llist.remove_node(3)
    print("List: ", llist)


def remove_dupes(llist):
    seen_nodes = set()
    for node in llist:
        if node.data in seen_nodes:
            llist.remove_node(node.data)
        else:
            seen_nodes.add(node.data)
    print("List without dupes: ", llist)


def partition(llist, partition):
    part_llist = LinkedList()

    for node in llist:
        if node.data < partition:
            head.next = node
            head = node
        else:
            tail.next = node
            tail = node
    tail.next = None
    print("Paritioned list: ", llist)


# Main Entry point
def main():
    llist = LinkedList()
    # fill_llist(llist)
    fill_llist_nums(llist)
    # remove_dupes(llist)
    partition(llist, 3)


# Handle running main from terminal, restrict execution of code for imports
if __name__ == "__main__":
    main()
