"""
PALINDROME PERMUTATION
Input: A string
Output: Is the string a permutation of a palindrome
"""

# Brute force
# Time complexity = Factorial in length of word
# Space complexity = Array of length factorial of number of characters


def brute_pal_perm(word: str) -> bool:
    print("Calculate all possible permutations of palindromes of length word")
    print("Check if the string is a permutation of such a palindrome")
    return True

# Optimal solution
# Observe that by definition, permutations of palindromes are
# words where no more than one character has an odd count
# Construct a character frequency table
# Check whether any character has odd count

# Optimisations : track odd as you go, use bit vectors instead of count, bit manipulation rather than iteration.


def optimal_pal_perm(word: str) -> bool:
    char_count = dict()
    odd_count = 0
    # Populate frequency map
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Determine odd count
    for char in word:
        if (char_count[char] % 2) == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


def main():
    print("Main")


if __name__ == "__main__":
    main()
