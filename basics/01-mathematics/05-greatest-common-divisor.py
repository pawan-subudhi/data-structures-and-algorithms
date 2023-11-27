"""
    Problem Statement:
        1. Find the greatest commom divisor of 2 numbers (i.e. nothing but finding HCF)
        2. Real life problem statement can be we have a floor of 4*6 then find the max size of each tile to fill the floor i.e.GCD(4,6) = 2

    Concept:
        1. For 2 numbers the divisor can be many but we need to find the greatest / highest among them
        2. Point to be observed if among 2 numnbers 1 is able to divide the other than the GCD will be that number itself
        3. If co-primes then the GCD is 1
"""
# code below
"""
    Naive approach:
        1. Find the min of 2 numbers and go down till we find the divisor that divides both
        2. Time - O(min(a,b)), Space - O(1)
"""


def naive_gcd(a, b):
    # The initial value of gcd should be the minimum of a and b.
    gcd = min(a, b)

    # The range function should start from gcd and go down to 1.
    for i in range(gcd, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    return gcd


"""
    Euclidean Algo Approach -
        1. The concept behind the Euclidean algorithm is based on the observation that the GCD of two numbers remains the same if you subtract the smaller number from the larger number repeatedly
        2. By continuously subtracting the smaller number from the larger number, we're effectively reducing the problem to a smaller problem while keeping the GCD unchanged.

        The time complexity of the `euclidean_gcd` function you provided is not as efficient as the standard Euclidean algorithm. In the worst case, where `a` and `b` are coprime (having no common factors), the while loop could run for a long time, potentially as long as max(a, b).

        The time complexity is best described as O(max(a, b)) in the worst case, which is much less efficient than the standard Euclidean algorithm's O(log(min(a, b)) time complexity.

        In terms of space complexity, the function uses a constant amount of memory (O(1)) because it modifies the values of `a` and `b` in place and does not create additional data structures. So, the space complexity is efficient.

        For GCD calculations, it's recommended to use the standard Euclidean algorithm for its efficiency and reliability, rather than the function you provided.
"""


def euclidean_gcd(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a

    return a


"""
    optimized euclidean algo:
        Time Complexity: The time complexity of this optimized Euclidean algorithm is very efficient and can be expressed as O(log(min(a, b))). It significantly reduces the number of iterations required compared to the subtraction-based approach. The algorithm works by taking remainders, and it takes the smaller of the two numbers and divides it repeatedly until one of them becomes zero.

        Space Complexity: The space complexity is determined by the depth of the recursive calls. In the worst case, when a and b are coprime (i.e., the GCD is 1), the function will recurse to a depth of log(min(a, b)). Therefore, the space complexity is O(log(min(a, b))).

        This optimized recursive Euclidean algorithm is the preferred method for calculating the GCD of two numbers due to its efficiency and low space requirements.
"""


def optimized_euclidean_gcd(a, b):
    if b == 0:
        return a

    return optimized_euclidean_gcd(b, a % b)


if __name__ == "__main__":
    input_str = input("Enter two numbers separated by a space: ")
    # Split the input by space and convert to integers
    num1, num2 = map(int, input_str.split())

    print(naive_gcd(num1, num2))
    print(euclidean_gcd(num1, num2))
    print(optimized_euclidean_gcd(num1, num2))
