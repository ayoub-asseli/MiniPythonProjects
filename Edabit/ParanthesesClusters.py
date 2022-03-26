"""
Write a function that groups a string into parentheses clusters. Each cluster should be balanced.

Examples:

split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
"""


def split(txt):
    res, i, c = [], 0, ''
    while i < len(txt):
        if txt[i] == '(':
            c += txt[i]
            i += 1
            continue
        else:
            while txt[i] == ')' or c.count('(') != c.count(')'):
                c += txt[i]
                i += 1
                if i == len(txt):
                    break
        res.append(c)
        c = ''
    return res
