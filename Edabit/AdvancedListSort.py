"""
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
"""

from collections import OrderedDict

def advanced_sort(lst):
    s = OrderedDict.fromkeys(lst)
    res = []
    for item in s:
        indexes = [i for i,val in enumerate(lst) if val==item]
        c = []
        for index in indexes:
            c.append(lst[index])
        res.append(c)
    return res
