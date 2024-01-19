"""
    Problem Statement:
        1. We are given a list of different coin types, assume we have infinite suupply of each coin types. Given an sum, our task is to find out different ways so that we can generate the sum.
        2. I/P: coins = [1,2,3]
           O/P: 4 [1+1+1+1, 2+2, 3+1, 2+1+1]

    Concept:
        1. We consider 2 choices for every coin
            - included
            - not included
        We return the sum of the results of the 2 recursive calls
"""
# code below
"""
    using normal recursion
    TC: exponential 2^n, n is the height of the tree
"""
def count_ways(coins, n, s):
    # if s == 0 means we found a solution so consider 1 way, if sum 0 and irrespective coins there or not the solution is possible
    if s == 0:
        return 1
    # if including element makes the sum go -ve then return 0
    if s < 0:
        return 0
    # we can't have solutions if we have some balance sum and no elements left so return 0
    if n == 0:
        return 0
    # sice we have been said that we have infinite number of coins in each type so we are not reducing the count of number of each coins
    return count_ways(coins, n, s-coins[n-1]) + count_ways(coins, n-1, s)


"""
    using DP to solve this
    - we know the number of params changing in the recursion is the number of dimensional list will be created

    TC: Theta(ns) # such solutions where TC dependent upon certain value and not polynomial are called PSEUDO POYNOMIAL SOLUTIONS, because if s value is high then the solution TC will be >>> high
    SC: Theta(ns)

"""
def count_ways_tabulation(coins, s):
    n = len(coins)
    # no of rows is s+1 and no of rows is n+1
    tabulation = [[0] * s for i in range(n+1)]

    # since with sum = 0 then count of ways will be 1 irrespective the no or type of coins, in the tabulation table marking the first column as 1
    for i in range(n+1):
        tabulation[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, s+1):
            # simply ignore the last coin
            tabulation[i][j] = tabulation[i-1][j]

            # when last coin is considered, but before that check is the last coin value is with the sum value left if >= then add up to the value
            if j >= coins[i-1]:
                tabulation[i][j] += tabulation[i][j-coins[i-1]]

    return tabulation[n][s]