"""

Create a function that takes a number num and returns each place value in the number.

Examples
num_split(39) ➞ [30, 9]

num_split(-434) ➞ [-400, -30, -4]

num_split(100) ➞ [100, 0, 0]

"""

def num_split(num):
    sign, num = str(num), str(num).replace('-', '')
    res = []
    i = len(num)-1
    for f in num:
        res.append(int(f + '0'*i))
        i -= 1
    return res if sign[0] != '-' else list(map(lambda x: -x, res))
