"""
Create a function that returns a list containing the prime factors of whatever integer is passed to it.

Examples
prime_factors(20) ➞ [2, 2, 5]

prime_factors(100) ➞ [2, 2, 5, 5]

prime_factors(8912234) ➞ [2, 47, 94811]
"""

def prime_factors(num):
    f = []
    i = 2
    while i**2 <= num:
        if num%i:
            i += 1
        else:
            num //= i
            f.append(i)
    if num > 1:
        f.append(num)
    return f
