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
