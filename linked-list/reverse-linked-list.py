# Q2: reverse a linked list in a single pass
# INPUT: Head of a linked list
# OUTPUT: Head of reversed linked list


def reverseLinkedList(head):
    prev = head
    current = head.next
    nextNode = head.next.next
    while current:
        current.next = prev
        prev = current
        current = nextNode
        nextNode = nextNode.next
    head.next = None
    return prev