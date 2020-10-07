# Q1: check if a list has a cycle
# INPUT: Head of a linked list
# OUTPUT: Boolean - True if the list has a cycle

# Assume that node values are integers / characters
# Floyd Cycle finding Algorithm
def checkListCycle(head):
    current = head
    while current:
        if current.val == True:
            return True
        else:
            current.val = True
    return False


"""
q2
A group of friends want to buy a bouquet of flowers. 
The florist wants to maximize his number of new customers and the money he makes.
To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1.
The first flower will be original price, (0+1) * OG PRICE, the next will be(1+1) * OG PRICE and so on.

Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers.
"""

# Complete the getMinimumCost function below.
# c = costs array
# k = number of people
# Find cheapest cost to buy all flowers

# INPUT: costs array of each flower, number of people (transactions)
# OUTPUT: Cheapest cost


def getMinimumCost(k, c):
    total = 0
    cycle = 0
    transactions = 0
    for i in range(len(c)):
        if transactions == k:
            transactions = 0
            cycle += 1
        cost = c.pop(max(c))
        total += cost * (1+cycle)
        transactions += 1
    return total


"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! 
There are a number of people queued up, and each person wears a sticker
indicating their initial position in the queue. 
Initial positions increment by 1 from 1 at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker
denoting their original places in line. One person can bribe at most two others. For example, if n==8  and Person 5 bribes Person 4 , the queue will look like this: 
[1,2,3,5,4,6,7,8]

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
"""

# INPUT: A queue representing state after bribes in original queue
# OUTPUT: Minimum number of bribes to produce queue or "Too Chaotic"

# Complete the minimumBribes function below.


def minimumBribes(q):
    expected = 1
    one_bribe = 2
    two_bribes = 3
    bribes = 0
    for i in range(len(q)):
        if q[i] == expected:
            expected = one_bribe
            one_bribe = two_bribes
            two_bribes += 1
        elif q[i] == one_bribe:
            bribes += 1
            one_bribe = two_bribes
            two_bribes += 1
        elif q[i] == two_bribes:
            bribes += 2
            two_bribes += 1
        else:
            return "Too Chaotic"
    return bribes
