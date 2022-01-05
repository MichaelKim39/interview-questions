# ArrayList JAVA = List PYTHON
# Hashmap JAVA = Dictionary PYTHON
# StringBuilder JAVA = String.join(List) PYTHON


# StringBuilder in Python
def string_builder():
    stringList = []
    for i in range(10):
        stringList.append("String")
    return ''.join(stringList)

# Check if every character in an ASCII sring is unique
# Return false if word exceeds length 256 (Unique extended ASCII characters)
# Recall hashmap lookup and insertion is constant time average case


def unique_chars(word):
    if (len(word) > 256):
        return False
    else:
        chars = dict()
        for i in range(len(word)):
            if (word[i] in chars):
                return False
            else:
                chars[word[i]] = True
    return True

# Check if two strings are permutations of each other


def check_perm(first, second):
    print(first)
    print(second)
    char_count = dict()
    if (len(first) != len(second)):
        print("Inequal length")
        return False
    for char in first:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in second:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True

# Check if permutation of word is palindrome
# Palindrome permutations must have at most one character with uneven count
# Linear runtime


def palindrome_perm(word):
    char_count = dict()
    odd_count = 0
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in word:
        if (char_count[char] % 2) == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


# Main entry point


def main():
    # print(string_builder())
    # print(unique_chars('abcdefgh'))
    # print(check_perm('hello', 'helll'))
    print(palindrome_perm('tacocat'))


# Handle running main from terminal, restrict execution of code for imports
if __name__ == "__main__":
    main()
