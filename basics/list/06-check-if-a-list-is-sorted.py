"""
    Problem Statement:
        1. Check is a list is sorted(Asc order) or not.
"""
# code below

def check_if_list_is_sorted(numbers):
    if len(numbers) <= 1:
        return True

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    else:
        return True

'''
    Another Approach:
        - We can use sorted(list) function instead of list.sort()
        - The main difference is the former one returns a new sorted list but the later modifies the same list in the order defined.

        The time complexity of the `sorted()` function in Python is O(n log n), where n is the number of elements in the input iterable. This is because `sorted()` uses a sorting algorithm, and the typical time complexity of comparison-based sorting algorithms (such as the one used by Python's `sorted()`) is O(n log n).
'''
def check_if_list_is_sorted_v2(numbers):
    sorted_list = sorted(numbers)
    if numbers == sorted_list:
        return True
    else:
        return False


if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    print(check_if_list_is_sorted(input_list))
    print(check_if_list_is_sorted_v2(input_list))

