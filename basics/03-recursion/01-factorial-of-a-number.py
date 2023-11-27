"""
    Problem Statement:
        1. Passed is an integer, need to find the factorial of that number
"""
# code below
def factorial_of_a_number(n):
    if n <= 0:
        return 1

    return n * factorial_of_a_number(n-1)

if __name__ == "__main__":
    # l = [int(x) for x in input().split()]
    n = int(input("Enter a number: "))

    print(factorial_of_a_number(n))

