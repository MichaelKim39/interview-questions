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
