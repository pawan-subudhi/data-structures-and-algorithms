"""
    Problem Statement:
        1. Takes a list of integers and a number, need to return a new list of integers which are less than the passed numbers.
        2. Not equal strictly less
"""
# code below
def elements_lesser_than_element(numbers, target_elemnt):
    output = []

    for number in numbers:
        if number < target_element:
            output.append(number)

    return output

def elements_lesser_than_element_v2(numbers, target_element):
    # achieve the same result more succinctly using a list comprehension.
    return [number for number in numbers if number < target_element]


def elements_lesser_than_element_v3(numbers, target_element):
    '''
        use the filter() function along with a lambda function to achieve the same result.

        lambda x: x < target_element is an anonymous function (lambda function) that returns True for elements less than target_element.
        filter() is used to filter the elements from numbers based on the condition defined by the lambda function.
        list() is used to convert the filter object to a list, producing the final result.

        This approach is functionally equivalent to the list comprehension version but uses the filter() function instead.

        Note:
            filter(function, iterable): It takes a function and an iterable. The function is applied to each element in the iterable, and only the elements for which the function returns True are included in the resulting iterator.

            list(iterator) constructs a list from the elements produced by the iterator. It iterates over the elements until exhaustion, collecting them into a list.
    '''
    return list(filter(lambda x: x < target_element, numbers))


if __name__ == "__main__":
    input_str = input("Enter numbers seperated by a space: ")
    input_list = list(map(int, input_str.split()))

    target_element = int(input("Enter the number, lesser than which we will dump the output: "))

    print(elements_lesser_than_element(input_list, target_element))
    print(elements_lesser_than_element_v2(input_list, target_element))
    print(elements_lesser_than_element_v3(input_list, target_element))
