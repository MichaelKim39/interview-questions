# q2 find 3rd element from last in linked list (single pass)
# INPUT: head of linked list
# OUTPUT: 3rd from last node value
# INFO: Linked list may not have more than 3 nodes

def thirdFromLast(head):
    # Traverse to third node OR throw error
    dummy = head
    third = None
    if head.next and head.next.next:
        third = head.next.next
    else:
        return "ERROR - Less than 3 Nodes"
    current = third
    third_last = head

    while current:
        current = current.next
        third_last = third_last.next

    return third_last.value