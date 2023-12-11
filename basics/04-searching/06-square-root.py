"""
    Problem Statement:
        1. Given a number need to find out the root of the number, if no perfect square root then return floor sqaaure root.
"""
# code below
'''
    Naive approach:
        TC: O(root(x))
        SC: O(1)
'''
def sqroot_floor(number):
    i = 1
    while(i * i <= number):
        i+= 1

    return i - 1


'''
    Efficient approach:
        TC: O(logn)
        SC: O(1) since iterative is used

        1. We will be using BS for finding it with 1 and low and n i.e. given number as high

'''
def efficient_sqroot_floor(number):
    low= 1
    high = number
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        mid_sqr = mid * mid

        if mid_sqr == number:
            return mid
        elif mid_sqr > number:
            high = mid - 1
        elif mid_sqr < number:
            low = mid + 1
            ans = mid # since ou target is to get the floor value everytime

    return ans


if __name__ == "__main__":
    n = int(input("Enter number: "))

    print(sqroot_floor(n))
    print(efficient_sqroot_floor(n))
