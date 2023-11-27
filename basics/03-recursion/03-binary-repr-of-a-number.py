"""
    Problem Statement:
        1. Given an integer, find the binary representation of the number

    Concept:
        1. Keep the number dividing by 2 and keep track of the remainder until we get the number as 0
        2. First do the recursion call and then do print then for the final output need to reverse the output
        3. If we are doing the tail recursion then don't need to reverse the output
"""
# code below
def binary_repr_of_a_number(n):
    if n==0:
        return

    binary_repr_of_a_number(n//2)
    print(n%2)

if __name__ == "__main__":
    n = int(input("Enter number: "))
    binary_repr_of_a_number(n)


