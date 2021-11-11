# INPUT: total MONEY in pool, array of ice cream flavour COST
# OUTPUT: 1 Indexed IDs of the unique pair of flavours costing total MONEY, E.g. "1 3"
# EXAMPLE: IN: MONEY = 5, COSTS = [2,1,3,5,6] => OUTPUT = "1 3"

def whatFlavors(cost, money):
    # (costValue: ID)
    costMap = dict()
    for i in range(len(cost)):
        complement = money - cost[i]
        if complement in costMap:
            return "" + (i+1) + " " + costMap(complement)
        else:
            costMap[cost[i]] = i+1
