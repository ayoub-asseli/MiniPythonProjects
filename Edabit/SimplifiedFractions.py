"""
Create a function that returns the simplified version of a fraction.

Examples
simplify("4/6") ➞ "2/3"

simplify("10/11") ➞ "10/11"

simplify("100/400") ➞ "1/4"

simplify("8/4") ➞ "2"

"""

def simplify(txt):
    txt = txt.split('/')
    def gcd(a, b): 
        if(b == 0): 
            return a 
        else: 
            return gcd(b, a % b) 
    d = gcd(int(txt[0]), int(txt[1]))
    return str(int(txt[0])//d) + "/" + str(int(txt[1])//d) if int(txt[1])//d != 1 else str(int(txt[0])//d)
