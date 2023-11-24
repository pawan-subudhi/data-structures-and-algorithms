"""
    Problem Statement:
        1. Count the number of digits present in the number

    Hint:
        1. Use floor division

    Concept:
        1. The idea is to use the floor division. if we divide the number by 10 the last digit is removed.
        2. If we keep dividing the number by 10 until the number becomes 0. The number of times we did division is the number of digits in number.
"""
# code below
n = int(input("Enter number: "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1

print("Count of digits is " + str(count))
