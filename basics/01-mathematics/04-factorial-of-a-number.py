"""
    Problem Statement:
        1. Find the factorial of a number
"""
# code below
# Iterative way: Time - O(n), Space - O(1)


def iterative_factorial(n):
    res = 1

    # since the endpoint is exclusive to n+1
    for i in range(2, n+1):
        res = res * i

    return res

# recursive approach: Time - O(n), Space - O(n)


def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)


if __name__ == "__main__":
    number = int(input("Enter number: "))
    print(iterative_factorial(number))
    print(recursive_factorial(number))
