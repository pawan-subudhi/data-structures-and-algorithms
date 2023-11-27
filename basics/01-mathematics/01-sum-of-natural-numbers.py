"""
    Problem Statement:
        1. Find the sum of first n natural numbers

    Hint:
        1. Will use the formulaL n*(n+1)/2
        2. If you want to display only int value instead of float then use // instead of /
"""
n = int(input("Enter n: "))
sum = n*(n+1)/2
print("Sum is: " + str(sum))
