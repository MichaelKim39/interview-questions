# INPUT: Sorted linked list head
# OUTPUT: Sorted linked list with duplicates removed head
# INFORMATION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head.next
        prev = head

        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next

        return head
