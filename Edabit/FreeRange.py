"""
Create a function which converts an ordered number list into a list of ranges (represented as strings). Note how some lists have some numbers missing.

Examples
numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]

numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]

numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]

numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

"""

def numbers_to_ranges(l):
    i = 0
    res = []
    l.append(0)
    L = [l[0]]
    for i in range(len(l)-1):
        if l[i+1] == l[i] +1:
            L.append(l[i+1])
        else:
            if len(L) > 1:
                res.append("{}-{}".format(L[0], L[-1]))
                L = [l[i+1]]
            else:
                res.append("{}".format(L[0]))
                L = [l[i+1]]
    return res
