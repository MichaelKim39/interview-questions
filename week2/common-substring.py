# INPUT: 2 strings
# OUTPUT: "Yes" or "No" based on common substring

# EXAMPLE: "Be" "Catt" - No common substring

"""
HASH TABLE: (Char, Status)
FIRST STRING: (B, true), (E, true)
SECOND STRING: CHECK HASH TABLE VALUES == true ? substring
"""


def commonSubstring(str1, str2):
    # Initialise hash table
    read_characters = dict()
    # Populate hash table with first string chars
    for char in str1:
        read_characters[char] = True
    # Check read chars common with the second string chars
    for char in str2:
        if read_characters[char]:
            return "Yes"
    return "No"
