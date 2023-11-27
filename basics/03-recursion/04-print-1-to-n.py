"""
    Problem Statement:
        1. Given an integer need to print 1 to n
"""
# code below

def print_1_to_N(n):
    if n <= 0:
        return

    print_1_to_N(n-1)
    print(n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_1_to_N(n)


