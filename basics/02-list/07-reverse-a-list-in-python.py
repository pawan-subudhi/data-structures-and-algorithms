"""
    Problem Statement:
        1. Reverse the input list passed

    Hint:
        1.
"""
# code below

# TC: O(n)
def reverse_list(numbers):
    i = 0
    j = len(numbers) - 1

    while i < j:
        l[i], l[j] = l[j], l[i] # In Python, the assignment statement l[i], l[j] = l[j], l[i] is an example of tuple unpacking. The right-hand side creates a temporary tuple with the values of l[j] and l[i], and then the values are assigned back to l[i] and l[j].
        i+=1
        j-=1

    return numbers

if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    print(reverse_list(input_list))

    # since the inbuilt function reverses the list inplace so if we difrectly print it will return None, so 2 step process
    input_list.reverse() # we can only revers the mutable objects using this. tuple can't be since its immutable or a string
    print(input_list)

    l = [1,2,3,4]
    print(list(reversed(l)))
    print(l[::-1])