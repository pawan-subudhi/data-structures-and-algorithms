"""
    Problem Statement:
        1. Given an sorted integer array need to remove the duplicates.
"""
# code below
# TC: O(n), SC: O(n)
def remove_duplicates_naive_approach(numbers):
    if not numbers:
        return numbers

    temp = [0] * len(numbers)
    temp[0] = numbers[0]

    res = 1
    for i in range(1, len(numbers)):
        if temp[res-1] != numbers[i]:
            temp[res] = numbers[i]
            res += 1

    # the process of updating numbers[:res] = temp[:res] effectively removes the extra elements from the original list (numbers). The slicing notation [:res] ensures that only the first res elements of numbers are replaced with the unique elements from the temporary list (temp).
    numbers[:res] = temp[:res]  # Update only the first 'res' elements

    return res

# TC: O(n), SC: O(1)
def remove_duplicates_efficient_approach(numbers):
    if not numbers:
        return numbers

    res = 1
    for i in range(1, len(numbers)):
        if numbers[res-1] != numbers[i]:
            numbers[res] = numbers[i]

            res += 1

    return res

if __name__ == "__main__":
    input_str = input("Enter numbers separated by a space: ")
    input_list = list(map(int, input_str.split()))

    print(remove_duplicates_naive_approach(input_list))
    print(remove_duplicates_efficient_approach(input_list))
