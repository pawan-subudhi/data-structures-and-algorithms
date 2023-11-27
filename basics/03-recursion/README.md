# Recursion

- Using solution of sub-problems to solve the solution of a bigger problem.

## Application of Recursion

1. Many algo techniques are based on Recursion:

- Dynamic Programming
  - Generally, we try to write Recursive solution and if we see any overlapping sub-problems we optimize then by using DP (either by memorization or tabulation).
  - Standard DP problems - LCS, Edit Distance
- Backtracking
  - They inherently recursion in nature (i.e. easy to write recursion solution than trying to write equivalent iterative code).
  - When we solve problems like rat in a maze, n-queen problem
- Divide and Conquer (Binary Search, Merge and Quick Sort)
  - These are mostly implemented using recursion.

2. Many problems inherently Recursive: (i.e. easy to write recursion solution than trying to write equivalent iterative code).

- Tower of honai
- DFS based traversals (Preorder / Inorder / Postorder of tree or DFS of graph)

# Tail Recursion

A Recursive function is called tail recursion, if the function does not do anything afte the Recursive call.

```
    def func(n):
        if n == 0:
            return
        print(n)
        func(n-1) # tail recursion
```

- In many languages we have tail elemination optimization like in c and c++, where it removed the recursion call instead do below

```
    def func(n):
        start:
            if n == 0:
                return
            print(n)
            n = n - 1
            goto start
```

- In python its not the same, python leaves on the coder to optimize and doesn't do of its own. So, we need to convert the tail recursion code to while loop as below

```
    def func(n):
        while n != 0:
            print(n)
            n -= 1
```

### Standard Example of Tail Recursion:

1. Quick Sort:
   - Tail Recursion Elmiination happpens, its the reason the quick sort is more optimized than the merge sort (as merge sort we don't have any tail Recursion)
2. Postorder Tree Traversal
