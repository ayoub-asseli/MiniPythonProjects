"""
The Farey sequence of order n is the set of all fractions with a denominator between 1 and n, reduced and returned in ascending order. 
Given n, return the Farey sequence as a list, with each fraction being represented by a string in the form "numerator/denominator".
"""

from itertools import combinations

def farey(a):
    g = lambda x: str(x[0]) + '/' +str(x[1])
    f = lambda x : int(x.split('/')[0]) / int(x.split('/')[1])
    L = sorted(list(map(g, list(combinations(range(1,a+1), 2)))), key= f)
    new_L = list(map(f, L))
    indices = []
    for i in range(len(new_L)-1):
        indices += [j for j, x in enumerate(new_L) if x == new_L[i]][1::]
    return ['0/1'] + [n for n in L if L.index(n) not in indices] + ['1/1']
