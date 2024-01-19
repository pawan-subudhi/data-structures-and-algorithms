# Dynamic Programming

1. It's basically an optimisation over the plain recursion.
2. In recursion we use the solutions of sub-problems i.e. solving the smaller peroblems to solve the bigger problem.
3. DP comes into a picture where in recursion we are solving the exact same some sub-problem again and again we can use DP to store the solutions of sub-problems and use it when required in future.

## The idea of DP is to reuse the solutions of sub-problems when there are overlapping sub-problems

## Depending upon the number of parameters changing in the recrusive function / call that many Dimensional list / array we will be creating for storing the values

# 2 Ways of implememting DP:

1. Memoization (Top Down)
   - Similar to that of recusrsion.
   - Easy to write compared to tabulation approach
   - Store Solutions and before proceeding further, check is already computed
   - Depending upon the number of parameters changing in the recrusive function / call that many Dimensional list / array we will be creating for storing the values
2. Tabulation (Bottom Up)
   - We need to solve the smaller problems first and then use it for bigger problems
   - Don't require the overhead of recursion calls
   - Implementing this approach is little harder than that of Memoization, in the memoizations its simple recursion and having a lookup in the memo table

# Applications of DP in real life probems:

1. Bellman Ford Algorithm (Shortest path from source to all the destination) -
   1. This algo is used in routing
2. Floyd Warshall Algorithm (Shortest path between every pair of vertices in a graph)
3. Diff Utility (LCS - Longest Common Subsequence)
   1. This is something which we use in our day to day life i.e. to know the differences in 2 file.
   2. We use in GIT
4. Search closed words (Edit distance) -
   1. We have dict of words, and searching a word which is not there is the dictionary may be mistyped. And we want to find the closest word of the given wrong word
5. Resorce Allocation (0-1 knapsack)
   1. We have some financial constraints, we have some budget and we have some things to acquire.
   2. Need to take decision over acquiring the thing or not.
