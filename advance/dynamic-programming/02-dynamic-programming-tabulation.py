"""
    Problem Statement:
        1. We need to write a code that returns the value of nth number in the fibonacci series
        2. Need to use DP's tabulation technique
        3. I/P: n = 3
           O/P: 2 (As fibonacci series: 0, 1, 1, 2, 3, 5,...)
"""
# code below
def fib_tabulation(n):
    dp = [None] * (n+1) # since we want to have nth fib nunber
    dp[0] = 0
    dp[1] = [1]

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]