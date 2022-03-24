"""
The Collatz sequence is as follows:

Start with some given integer n.
If it is even, the next number will be n divided by 2.
If it is odd, multiply it by 3 and add 1 to make the next number.
The sequence stops when it reaches 1.

According to the Collatz conjecture, it will always reach 1. If that's true, you can construct a finite sequence 
following the aforementioned method for any given integer.
Write a function that takes in an integer n and returns the highest integer in the corresponding Collatz sequence.
"""

def collatz(a, b):
    while a != 1 and b != 1:
        if a%2 == 0:
            a = a//2
        else:
            a = a*3 + 1
        steps_a += 1
        if b%2 == 0:
            b = b//2
        else:
            b = b*3 + 1
        steps_b += 1
    return "a" if a == 1 else "b"
