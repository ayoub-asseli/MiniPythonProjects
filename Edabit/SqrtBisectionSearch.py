"""
Create a function that uses bisection search to compute the approximative value of the square root of a number.

Use any integer or float as an argument.
Use a delta variable of 0.01 to know when a result is valid (i.e. if the result squared is between n - delta and n + delta, it's considered valid).
Examples
bisec_sqrt(69) ➞ 8.307

bisec_sqrt(16) ➞ 4.0

bisec_sqrt(12984771) ➞ 3603.439

bisec_sqrt(12.21) ➞ 3.494
"""


def bisec_sqrt(n):
  a, b, c = 0, n, 0
  while abs(c ** 2 - n) > 0.01:
    c = (a + b) / 2
    if c ** 2 > n:
      b = c
    elif c ** 2 < n:
      a = c
  return round(c, 3)
