# Input: string
# Output: Is every character in the string distinct?

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
