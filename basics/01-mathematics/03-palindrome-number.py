"""
    Problem Statement:
        1.These are the numbers if we iterate from L to R or R to L we get the same number

    Hint:
        1.Traverse the original number and generate the rev number and compare both
"""
# code below
# Approach 1


def is_pal(n):
    rev = 0
    temp = n
    while temp:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10

    return rev == n


# Approach 2
'''
The time complexity of the given code to check if a number is a palindrome is O(n), where "n" is the number of digits in the input number.
Here's a breakdown of the time complexity:
1. Converting the number to a string takes O(n) time, where "n" is the number of digits in the number.
2. Reversing the string using slicing takes O(n) time, as it iterates through the characters in the string.
3. Comparing the original string to the reversed string also takes O(n) time in the worst case because it involves comparing each character.
So, each step in the process has a time complexity of O(n), and because they are sequential, the overall time complexity is still O(n).
'''


def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    return number_str == reversed_str


# Approach 3
'''
Doing in constant space
'''


def is_palindrome_with_constant_space(number):
    if number < 0:
        return False  # Negative numbers are not palindromes

    num_str = str(number)
    left = 0
    right = len(num_str) - 1

    while left < right:
        if num_str[left] != num_str[right]:
            return False  # Digits don't match; it's not a palindrome
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    number = 4554
    print(is_pal(number))
