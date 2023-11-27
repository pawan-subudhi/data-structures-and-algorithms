"""
    Problem Statement:
        1. We are given a list and need to left rotate the list by 1 (i.e. counter clockwise)
        2. ex: l = [10, 20, 30, 40] => [20, 30, 40, 10]
"""
# code below

def left_rotate_list_using_inbuilt_func(numbers):
    # approach 1
    res = numbers[1:] +  numbers[0:1]
    print("approach 1: %s" % res)

    # approach 2
    numbers.append(numbers.pop(0))
    print("approach 2: %s" % numbers)

def left_rotate_list_using_custom_func(numbers):
    temp = numbers[0]

    for i in range(1, len(numbers)):
        numbers[i-1] = numbers[i]

    numbers[len(numbers)-1] = temp

    return numbers

if __name__ == "__main__":
    # l = [int(x) for x in input().split()]
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    # left_rotate_list_using_inbuilt_func(input_list)
    print(left_rotate_list_using_custom_func(input_list))
