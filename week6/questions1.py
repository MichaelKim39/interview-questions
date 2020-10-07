# q1 find the first non repeated character of a given string
# INPUT: String of any characters
# OUTPUT: First non-repeated character

def firstNonRepeated(word):
    char_freq = dict()
    # Populate hashmap
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    # Find first non-repeated char
    for char in word:
        if char_freq[char] == 1:
            return char
    # Otherwise no unique chars
    return ""


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


# q3 find fibonacci numbers with a recursive solution (upto n)
# INPUT: integer N
# OUTPUT: Array of fibonacci nums upto N

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    fibs = [0, 1]
    for i in range(n):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]
