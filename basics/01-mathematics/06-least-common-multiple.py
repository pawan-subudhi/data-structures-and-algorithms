"""
    Problem Statement:
        1. Find the LCM of 2 numbers (i.e. a smallest number which is divisible by both the numbers)

    Hint:
        1.a*b = gcd(a,b) * lcm(a,b)
            We can use the above problem

    Concept:
        1. For 2 numbers the multiple can be many but we need to find the smallest / least among them
        2. Point to be observed if among 2 numnbers 1 is mutliple of other than the LCM will be the greater number
        3. If both the numbers are co-prime then the LCM will be a*b
"""
# code below
"""
    naive approach:
        Time Complexity: The time complexity of this function can be quite high in the worst case, especially if a and b are significantly different. It could potentially take a long time to find the LCM by repeatedly incrementing res. In the worst case, the time complexity is unbounded, but on average, it would be proportional to the product of a and b (O(a * b)).
        Space Complexity: The space complexity is constant (O(1)) because the function uses a fixed amount of memory regardless of the input values.
"""


def lcm(a, b):
    res = max(a, b)

    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1


"""
    Efficient approach:
        a * b = gcd(a,b) * lcm(a,b)

    The time taken will be the time to calculate the GCD
        Time Complexity: The time complexity of this function can be quite high in the worst case, especially if a and b are significantly different. It could potentially take a long time to find the LCM by repeatedly incrementing res. In the worst case, the time complexity is unbounded, but on average, it would be proportional to the product of a and b (O(a * b)).

        Space Complexity: The space complexity is constant (O(1)) because the function uses a fixed amount of memory regardless of the input values.
"""


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def optimized_lcm(a, b):
    return (a*b)//gcd(a, b)


if __name__ == "__main__":
    input_str = input("Enter 2 numbers sperated by a space: ")
    num1, num2 = map(int, input_str.split())

    print(lcm(num1, num2))
    print(optimized_lcm(num1, num2))
