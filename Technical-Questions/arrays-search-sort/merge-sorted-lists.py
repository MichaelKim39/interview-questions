# INPUT: List Head nodes of two SORTED linked lists
# OUTPUT: Single merged, sorted version of the two lists
# INFO: Lists not necessarily same length
# Example:
# 1 - 2 - 3 - 3
# 2 - 4 - 5 - 9
# 1 - 2 - 2 - 3 - 4 - 5 - 9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy

        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next
            dummy = dummy.next

        if l1 is not None:
            dummy.next = l1
        if l2 is not None:
            dummy.next = l2

        return head.next

    def mergeLists(self, l1, l2):
        current = ListNode()
        head = current

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 is not None:
            current.next = l1

        if l2 is not None:
            current.next = l2

        return head.next
