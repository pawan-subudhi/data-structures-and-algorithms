"""
    Problem Statement:
        1. Takes a list and returns 2 list by filtering even and odd numbers
"""
# code below
def get_even_odd(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 ==0:
            even.append(number)
        else:
            odd.append(number)

   # a function can return multiple value, if we return like below it essentially becomes a tuple
    return even, odd

if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    # unpack the tuple and display
    even, odd = get_even_odd(input_list)
    print(even, odd)