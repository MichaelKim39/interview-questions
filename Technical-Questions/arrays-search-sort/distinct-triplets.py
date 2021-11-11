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