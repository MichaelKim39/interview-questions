# Q1: check if a list has a cycle
# INPUT: Head of a linked list
# OUTPUT: Boolean - True if the list has a cycle

# Assume that node values are integers / characters
# Floyd Cycle finding Algorithm
def checkListCycle(head):
    current = head
    while current:
        if current.val == True:
            return True
        else:
            current.val = True
    return False





