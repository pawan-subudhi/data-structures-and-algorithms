"""
    Problem Statement:
        1. Takes an integer list and returns the larget element
"""
# code below

# TC: O(n^2)
def get_max_naive_approach(numbers):
    for x in numbers:
        for y in numbers:
            if y > x:
                break
        else:
            return x
    return None # if list empty then we return None

# TC: O(n)
def get_max_v1(numbers):
    return max(numbers)

# TC: O(n) - max() is inbuilt but lets see the logic behind it
def get_max_efficient(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]

    return max_value


if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    print(get_max_naive_approach(input_list))
    print(get_max_v1(input_list))
    print(get_max_efficient(input_list))
