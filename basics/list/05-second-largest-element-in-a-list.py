"""
    Problem Statement:
        1. Takes an integer array and need to find the second largest element from the list.

    Hint:
        1. In a single traversal try to store both
            lar = l[0]
            slar = None

            x > lar: slar = lar; lar = x
            x == lar: Ignore
            x < lar:
                slar >=  x: Ignore
                slar == None or x > slarg: slar = x
"""
# code below

def get_largest(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]

    return max_value

'''
    TC: O(n)
    - It's taking O(n) but requires 2 traversal
    - We will use the approach of finding the largest number
    - then will find the second largest
'''
def get_second_largest_naive_approach(numbers):
    if len(numbers) <= 1:
        return None

    largest = get_largest(numbers)
    second_largest = None
    for x in numbers:
        if x != largest:
            second_largest = x if second_largest == None else max(second_largest, x)

    return second_largest

'''
    TC: O(n)

    1. In a single traversal try to store both
        lar = l[0]
        slar = None

        x > lar: slar = lar; lar = x
        x == lar: Ignore
        x < lar:
            slar >=  x: Ignore
            slar == None or x > slarg: slar = x
'''
def get_second_largest_efficient_approach(numbers):
    if len(numbers) <= 1:
        return None

    lar = numbers[0]
    slar = None

    for x in numbers[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or x > slar:
                slar = x

    return slar

if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    print(get_second_largest_naive_approach(input_list))
    print(get_second_largest_efficient_approach(input_list))
