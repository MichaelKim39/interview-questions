"""
q1
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine
otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is NO.

give me one grand today night
give one grand today
YES

two times three is not four
two times two is four
NO

ive got a lovely bunch of coconuts
ive got some coconuts
NO
"""

# Complete the checkMagazine function below.

magazine: "give me one"
note: "give one"
word_freq: (give, 0), (me, 1), (one, 0)
current_word: "one"


def checkMagazine(magazine, note):
    # Parse magazine into frequency dictionary of (word: frequency) pairs
    word_freq = dict()
    current_word = ""
    magazine += " "
    for char in magazine:
        if char == " ":
            if word_freq[current_word]:
                word_freq[current_word] += 1
            else:
                word_freq[current_word] = 1
            current_word = ""
        else:
            current_word += char

    # Parse words from note and check validity
    note += " "
    for char in note:
        if char == " ":
            if word_freq[current_word]:
                word_freq[current_word] -= 1
                if word_freq[current_word] < 0:
                    return "No"
            else:
                return "No"
            current_word = ""
        else:
            current_word += char

    return "Yes"


# ---------------------------------------------------------------------------- #
#                                  QUESTION 2                                  #
# ---------------------------------------------------------------------------- #

"""
given 3 arrays a, b, c of different sizes, 
find the number of distinct triplets(p, q, r) such that p is in a, q is in b and r is in c AND p <= q and q >= r
sort arrays
remove repetitions
start from front - remove takes time

EXAMPLE:
res: 

a: [3, 5, 6]
b: [3, 6]
c: [4, 6, 9]

a: [3]
b: [3]
c: []

a: [a1, a2]
b: [b1]
c: [c1, c2]
All elements of a and all elements of c are less than element in b
Number of triplets = a x c


= > 4
reason: 4 triplets(3, 6, 4), (3, 6, 6), (5, 6, 4), (5, 6, 6)
"""
