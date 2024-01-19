"""
    Problem Statement:
        1. Given 2 strings, need to find the longest common subsequence (LCS)
        2. s1 = "ABCDGH"
           s2 = "AEDFHR"

           o/p - 3

    Hint:
        1.

    Concept:
        1. Subsequence is nothing but from a string we can take 1 or more characters either continous or not doesn't matter but the order need to be maintained
        2. no of subsequences for "CDA" -> 2^n, as per character 2 possibilities either consider or don't. NULL is also possible in this case no letters have been considereed
"""
# code below
"""
    The below code is the traditional recursion approach, its having multiple overlapping sub problems
    TC: 2^n exponential
"""
def lcs(s1, s2, n, m):
    # if any str gets empty then the lenght of common subsequence will be 0
    if m == 0 or n == 0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1 + lcs(s1, s2, n-1, m-1)

    return max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1))

"""
    Lets write a DP Memoization approach code
    TC: Theta(mn)
"""
M = 10
N = 10
memo = [[-1]*N for i in range(M)]

def lcs_memoization(s1, s2, n, m):
    if memo[n][m] != -1:
        return memo[n][m]
    if n == 0 or m == 0:
        return 0
    else:
        if s1[n-1] == s2[m-1]:
            memo[n][m] = 1+ lcs_memoization(s1, s2, n-1, m-1)
        else:
            memo[n][m] = max(lcs_memoization(s1, s2, n-1, m), lcs_memoization(s1, s2, n, m-1))

    return memo[n][m]

"""
    Below is the DP tabulation approach
    TC: Theta(mn)
"""
def lcs_tabulation(s1, s2):
    m = len(s1)
    n = len(s2)
    # extra column and extra row is for storing the LCS of length 0
    tabulation = [[None] * (n+1) for i in range(m+1)]

    for i in range (m+1):
        for j in range (n+1):
            if i == 0 or j ==0:
                tabulation[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                tabulation[i][j] = 1 + tabulation[i-1][j-1]
            else:
                tabulation[i][j] = max(tabulation[i-1][j], tabulation[i][j-1])

    return tabulation[m][n]


if __name__ == "__main__":
    s1 = "ABCDGH"
    s2 = "AEDFHR"

    print(lcs(s1, s2, len(s1), len(s2)))
    print(lcs_memoization(s1, s2, len(s1), len(s2)))
    print(lcs_tabulation(s1, s2)

"""
    Variations of LCS
    1. Diff Utility (Git is real life problem)
    2. Minimum insertions and deletions to convert s1 into s2
    3. Shortest common superquence
    4. Longest palindromic subsequence
    5. Longest repeating sequence
    6. Space optimised DP solutions of LCS
    7. Printing LCS
"""