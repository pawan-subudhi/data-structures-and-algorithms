"""
    Problem Statement:
        1. Find the a average / mean of elements of a list

    Concept:
        1. sum of all / no of element
"""
# code below
def avg_or_mean_of_list(numbers):
    sum = 0
    for number in numbers:
        sum += number

    n = len(numbers)
    return sum/n

def avg_or_mean_of_list_v2(numbers):
    return sum(numbers)/len(numbers)

if __name__ == "__main__":
    input_str = input("Enter numbers separated by a space: ")
    # Split the input by space and convert to integers
    int_list = list(map(int, input_str.split()))

    print(avg_or_mean_of_list(int_list))
    print(avg_or_mean_of_list_v2(int_list))