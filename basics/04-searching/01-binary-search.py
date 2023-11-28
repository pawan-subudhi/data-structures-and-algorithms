"""
    Problem Statement:
        1. Given a sorted integer list, need to find the number using binary search
"""
# code below
# TC: O(n), SC: O(1)
def binary_search_iterative(numbers, search_element):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_element:
            return mid
        elif numbers[mid] < search_element:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# TC: O(n), SC: O(logn)
def binary_search_recursive(numbers, search_element, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if numbers[mid] == search_element:
            return mid
    elif numbers[mid] < search_element:
        low = mid + 1
    else:
        high = mid - 1

    return binary_search_recursive(numbers, search_element, low, high)

if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    search_element = int(input("Enter search element: "))

    print(binary_search_iterative(input_list, search_element))

