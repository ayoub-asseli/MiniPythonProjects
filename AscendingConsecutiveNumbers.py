"""
Write a function that returns True if a string consists of ascending or ascending AND consecutive numbers.

Examples:

ascending("232425") ➞ True
# Consecutive numbers 23, 24, 25

ascending("2324256") ➞ False
# No matter how this string is divided, the numbers are not consecutive.

ascending("444445") ➞ True
# Consecutive numbers 444 and 445.
"""

def ascending(txt): 
    n = len(txt)
    for i in range(2, n-2):
        sub, sub_size = n, n//i
        res = list(map(lambda x: int(x), [txt[i:i+sub_size] for i in range(0, sub, sub_size)]))
        res2 = sorted(set(res))
        if res == res2 and (res2[-1] - res2[0] == len(res)-1):
            return True
    return False
