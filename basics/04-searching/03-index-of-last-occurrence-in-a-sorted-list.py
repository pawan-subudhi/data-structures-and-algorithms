"""
    Problem Statement:
        1. Given a sorted list as input. Need to find the index of last Occurrence in a Sorted list.
        2. The array may contain duplicate values
    Hint:
        1. Similar approach that of finding the last occurence of element in list.
"""
# code below
# TC: O(N), TC: O(1)
# Naive approach - Traverse the list and return the index when we find the last match. Else if goes till end and not find then return -1
def last_occurence_naive(numbers, search_element):
    for i in reversed(range(0, len(numbers))):
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
def last_occurence_efficient(numbers, search_element, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if numbers[mid] > search_element:
        high = mid - 1
    elif numbers[mid] < search_element:
         low = mid + 1
    else:
        # check if its the last occurence or not
        if ((mid == len(numbers) - 1) or (numbers[mid] != numbers[mid+1])):
            return mid
        # below handles if its not check on left so reducing high to mid - 1
        else:
            low = mid + 1

    return last_occurence_efficient(numbers, search_element, low, high)



if __name__ == "__main__":
    # l = [int(x) for x in input().split()]
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    search_element = int(input('Enter the element need to search: '))

    print(last_occurence_efficient(input_list, search_element, 0, len(input_list) - 1))

