"""
    Problem Statement:
        1. Given a sorted list as input. Need to find the index of First Occurrence in a Sorted list.
        2. The array may contain duplicate values
"""
# code below
# TC: O(N), TC: O(1)
# Naive approach - Traverse the list and return the index when we find the first match. Else if goes till end and not find then return -1
def first_occurence_naive(numbers, search_element):
    for i in range(0, len(numbers)):
        if numbers[i] == search_element:
                return i
    else:
         return -1

'''
    Efficient Approach:
        1. Wil use the binary search approach
        2. We have 2 ways : Recursive and Iterative
            The iterative is better as the SC: O(1) unlike recursion
'''
def first_occurence_efficient(numbers, search_element, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if numbers[mid] > search_element:
        high = mid - 1
    elif numbers[mid] < search_element:
         low = mid + 1
    else:
        # check if its the first occurence or not
        if mid == 0 or (numbers[mid] != numbers[mid-1]):
            return mid
        # below handles if its not check on left so reducing high to mid - 1
        else:
            high = mid - 1

    return first_occurence_efficient(numbers, search_element, low, high)



if __name__ == "__main__":
    # l = [int(x) for x in input().split()]
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    search_element = int(input('Enter the element need to search: '))

    print(first_occurence_efficient(input_list, search_element, 0, len(input_list) - 1))
