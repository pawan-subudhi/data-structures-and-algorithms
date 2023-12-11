"""
    Problem Statement:
        1.Given a sorted binary list of 0's and 1's need to find the count of 1's in it

    Hint:
        1. Use Binary search
"""
'''
    Naive approach:
        TC:O(n)

        1. Simply traverse from left to right and if found 1 stop and return the length
        2. If not travserse from right to left and if found 0 stop and return the length
'''

'''
    Efficient approach:
        TC: O(logn)
        1. find the first occurence of 1 using binary search
        2. return length
'''
# code below
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

def count_1s(numbers):
    first_occurence = first_occurence_efficient(numbers, 1, 0, len(numbers)-1)

    if first_occurence != -1:
        # (n-1) - first_occurence + 1 = (n - first_occurence)
        return len(numbers) - first_occurence

    return 0

if __name__ == "__main__":
    # l = [int(x) for x in input().split()]
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    print(count_1s(input_list))
