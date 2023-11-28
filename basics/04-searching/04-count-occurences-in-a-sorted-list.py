"""
    Problem Statement:
        1. Given a sorted list as input. Need to find the count of occurences in the sorted list
    Hint:
        1. Find the first, last occurence index using BS and do last - first + 1
"""
# code below
'''
    Naive Approach:
        1. Traverse the list and keep track of the count of element
        2. O(n)

    Better Approach:
        1. With simple Binary search find any occurence of that element and then do the linear traversal on both sides to get the count
        2. TC: O(logn) + O(n) = O(n)

    Efficient Approach:
        1. Wil use the binary search approach
        2. We have 2 ways : Recursive and Iterative
            The iterative is better as the SC: O(1) unlike recursion
        3. TC: O(logn)
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
        if ((mid == 0) or (numbers[mid] != numbers[mid-1])):
            return mid
        else:
            high = mid + 1

    return first_occurence_efficient(numbers, search_element, low, high)

def last_occurence_efficient(numbers, search_element, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if numbers[mid] > search_element:
        high = mid - 1
    elif numbers[mid] < search_element:
         low = mid + 1
    else:
        if ((mid == len(numbers) - 1) or (numbers[mid] != numbers[mid+1])):
            return mid
        else:
            low = mid + 1

    return last_occurence_efficient(numbers, search_element, low, high)

def count_occurences(numbers, search_element):
    first_occurence = first_occurence_efficient(numbers, search_element, 0, len(numbers) - 1)
    if first_occurence == -1:
        return 0

    last_occurence = last_occurence_efficient(numbers, search_element, 0, len(numbers) - 1)
    return last_occurence - first_occurence + 1

if __name__ == "__main__":
    # l = [int(x) for x in input().split()]
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    search_element = int(input('Enter the element need to search: '))

    print(count_occurences(input_list, search_element))

