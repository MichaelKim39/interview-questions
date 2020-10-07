# TODO: Complete
# INPUT: Head of a linked list, index M, index N
# OUTPUT: Head of a linked list whose elements from index M to N are reversed
# INFORMATION: Algorithm must only involve one pass of linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        current = head
        previous = None

        for _ in range(m-1):
            previous = current
            current = current.next
        tail = current
        con = previous

        for _ in range(n-m+1):
            third = current.next
            current.next = previous
            previous = current
            current = third

        if con:
            con.next = previous
        else:
            head = previous

        tail.next = current

        return head
