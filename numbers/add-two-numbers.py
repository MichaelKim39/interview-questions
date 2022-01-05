"""
INPUT: 
Heads of two non-empty linked lists representing non-negative integers
The lists store each digit in a node in reverse order
OUTPUT:
Sum of the integers as a linked list in reverse order
ASSUME:
No leading zeros unless the number is 0
"""

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

# Time complexity: O(number of digits)
# Space complexity: O(number of digits)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = 0
        second = 0
        total = 0
        # Extract first number as int
        i = 0
        while l1:
            first += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        # Extract second number as int
        i = 0
        while l2:
            second += l2.val * (10 ** i)
            l2 = l2.next
            i += 1
        # Create head for linked list of sum
        total = first + second
        total_head = ListNode()
        total_head.val = total % 10
        total //= 10
        # Populate linked list of sum
        current = total_head
        while total > 0:
            current.next = ListNode()
            current.next.val = total % 10
            current = current.next
            total //= 10
        # Return head
        return total_head


"""
IMPROVEMENTS:
1. Sum in one loop
2. Sum and transfer in one loop - done by maintaining carry bit
"""
