"""
    Problem Statement:
        1. Passed a string. Need to figure out whether or not the string is palindrome or not
"""
# code below
# TC: O(n), SC: O(n)
def palindrome_check(str_input, start, end):
    # below base case handles for the 0 or 1 characters left
    if start >= end:
        return True

    # the recursive call will only work if the first and last pointing characters are same
    return (str_input[start] == str_input[end] and palindrome_check(str_input, start + 1, end - 1))
if __name__ == "__main__":
    str_input = input("Enter string: ")

    print(palindrome_check(str_input, 0, len(str_input) - 1))
