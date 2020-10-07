# q1 given a string check if it is a palindrome

def checkPalindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

# q2 check if 2 strings are anagrams


def checkAnagram(word1, word2):
    char_map = dict()

    for char in word1:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    for char in word2:
        if char in char_map:
            char_map[char] -= 1
            if char_map[char] < 0:
                return False
        else:
            return False

    return True


# q3 find the middle element of a linkedlist in a single pass

def middleList(head):
    current, middle = head
    index = 1

    while current:
        current = current.next
        index += 1
        if index % 2 != 0:
            middle = middle.next

    return middle
