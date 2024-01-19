"""
    Problem Statement:
        1. We need to write a code that returns the value of nth number in the fibonacci series
        2. Need to use DP's memoization technique
        3. I/P: n = 3
           O/P: 2 (As fibonacci series: 0, 1, 1, 2, 3, 5,...)
"""
# code below
"""
    TC: Is exponential i.e. (golden ratio ^ n)
        - golden ratio = (1 + sqrt(5))/2

    - A simple recrusive solution with EXPONENTIAL TC
    - With memoization we will be optimise to LINEAR TC
"""
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

"""
    Code using Memoization idea
"""
memo = [None] * 100 # considering the max value of N can be 100
def fib_memoizatiion(n):
    if memo[n] != None:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib_memoizatiion(n-1) + fib_memoizatiion(n-2)

    return memo[n]

if __name__ == "__main__":
    n = int(input("Enter number: "))



