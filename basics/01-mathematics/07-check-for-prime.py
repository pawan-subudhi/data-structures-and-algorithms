"""
    Problem Statement:
        1. Check a number is prime (i.e. a number which is divisible by and 1 and itself)

    Hint:
        1. Divisors always appear in pairs.

    Concept:
        1. If a no is having some other factors (except 1 and itself) then its not a prime number and are called composite number
        2. 1 is not considered a prime number. By definition, a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. Since 1 does not meet the criteria of being greater than 1, it is not classified as a prime number.
        3. When you find the divisors of a number, they come in pairs except for the square root of the number.
        Let's consider a number N . If a is a divisor of N  (i.e. N is divisible by a ), then  b = N/a  is also a divisor because  N = a * b . This is true for all divisors of  N , except when  a = b , which happens when  a  is the square root of  N .

        In the context of finding prime numbers, this property is useful. When checking for the primality of a number, you only need to check divisibility up to the square root of that number. If a number is not a prime, it will have divisors, and at least one of those divisors will be less than or equal to its square root. Checking beyond the square root would involve redundant checks of divisors already considered.
"""
# code below
'''
naive approach:
    Time Complexity - O(n)
'''


def is_prime_naive(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


'''
Optimised Approach:
    Based upon the concept i.e. x,y are divisors pairs for N. If x <=y then x * x < N and hence x <= root(N)
    Time Complexity - O(root(n))
'''


def is_prime_optimised(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


'''
    Super optimised approach:
        This approach is more efficient than checking divisibility by every number up to n and is based on the observation that all prime numbers greater than 3 can be written in the form 6k ± 1. It eliminates many unnecessary checks, reducing the time complexity of the primality test.

        Time Complexity - O(root(n))
'''


def is_prime_super_oprtimised_approach(n):
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while(i * i <= n):
        # It increments i by 6 because the numbers 6k, 6k + 2, 6k + 4 are divisible by 2, and 6k + 3 is divisible by 3. So, checking i and i + 2 covers potential divisors.
        if (n % i == 0) or (n % (i + 2) == 0):
            return False

        i += 6

    return True


'''
    Note:
    Both `is_prime_optimised` and `is_prime_super_optimised_approach` functions are optimized compared to a basic trial division approach. However, the performance difference between them might not be substantial for small values of  n . Let's analyze each:

    1. **`is_prime_optimised`:**
    - It uses a straightforward trial division approach.
    - The loop iterates from  i = 2  to  \sqrt{n} .
    - Time Complexity:  O(sqrt{n})

    2. **`is_prime_super_optimised_approach`:**
    - It incorporates a more optimized trial division by checking divisors in the form  i  and  i + 2 .
    - The loop starts with  i = 5  and increments  i  by 6 in each iteration.
    - This approach skips numbers that are divisible by 2 and 3.
    - Time Complexity:  O(sqrt{n}/6) , effectively  O(sqrt{n})

    **Which one is better?**
    - For small values of  n , the difference might not be significant, and both approaches are reasonable.
    - The `is_prime_super_optimised_approach` is a bit more optimized due to skipping certain numbers in the loop, but the gain might not be substantial for small  n .

    In practical scenarios, especially when dealing with larger numbers, more advanced algorithms like the Sieve of Eratosthenes or probabilistic primality testing (e.g., Miller-Rabin) are often used for better performance.
'''

if __name__ == "__main__":
    n = int(input("Enter number to check whether is prime / not: "))
    print(is_prime_naive(n))
    print(is_prime_optimised(n))
    print(is_prime_super_oprtimised_approach(n))
