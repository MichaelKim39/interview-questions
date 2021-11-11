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
