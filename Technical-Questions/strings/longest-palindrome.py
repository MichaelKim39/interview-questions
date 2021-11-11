# q4 find the longest palindrome of a substring
def longest_palindrome(word):
    max_length = 1

    for index in range(len(word)-1):
        # First pass (check odd palindromes)
        local_max = 1
        left = index - 1
        right = index + 1
        while word[left] == word[right]:
            left -= 1
            right += 1
            local_max += 2
        max_length = max(local_max, max_length)

        # Second pass (check even palindromes)
        local_max = 0
        left = index - 1
        right = index

        while word[left] == word[right]:
            left -= 1
            right += 1
            local_max += 2
        max_length = max(local_max, max_length)
