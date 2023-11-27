"""
    Problem Statement:
        1. Given an intger, need to find the sum of digits of the number
"""
# code below
def sum_of_digits_of_a_number(n):
    if n < 10:
        return n

    return sum_of_digits_of_a_number(n // 10) + n % 10

if __name__ == "__main__":
    n = int(input("Enter number: "))

    sum_of_digits_of_a_number(n)
