# Q1: find value n in an array
# INPUT: Array
# OUTPUT: True if value n in array

def findValue(array, value, left, right):
    if left == right:
        if array[left] == value:
            return True
    if left >= right:
        return False
    mid = left + right // 2
    if value == array[mid]:
        return True
    elif value > array[mid]:
        return findValue(array, value, mid+1, right)
    elif value < array[mid]:
        return findValue(array, value, left, mid-1)


def findN(array, value):
    findValue(array, value, 0, len(array)-1)

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
