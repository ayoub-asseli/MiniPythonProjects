"""
First of all, some explanations about how a roman-numeral is built:
Rule 1 -> I, X and C cannot be repeated more than 3 times.
Rule 2 -> The digits V, L and D are not repeated. The repetition of V, L and D is invalid in the formation of numbers.
Rule 3 -> When a digit of lower value is written after a digit of higher value, the values of all the digits are added.
Rule 4 -> When a digit of lower value is written to the left or before a digit of higher value,
   then the value of the lower digit is subtracted from the value of the digit of higher value.
Rule 5 -> Any symbol that precedes a higher value symbol is subtracted from the latter
Rule 6 -> The symbols are grouped in descending order, except for the values to be subtracted according to the previous rule
"""

roman_numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

# Entry from user
user = input("Enter your Roman numbers: ")
n = len(user)

########################################################################################################################

# Validation process: Is the number valid ?

# Rule 1 ?
for i in range(n-3):
    L = user[i:i+4]
    if user[i] in "IXC" and L.count(user[i]) >= 4:
        print("\nEnter a valid Roman Numerals please....")
        exit()
# Rule 2 ?
for i in range(n-1):
    if user[i] in "VLD" and user[i] == user[i+1]:
        print("\nEnter a valid Roman Numerals please....")
        exit()

# Rule 5 ?
for i in range(n-1):
    if user[i] == "I" and user[i+1] not in "IVX":
        print("\nEnter a valid Roman Numerals please....")
        exit()
    elif user[i] == "V" and user[i+1] not in "I":
        print("\nEnter a valid Roman Numerals please....")
        exit()
    elif user[i] == "X" and user[i+1] not in "IVXLC":
        print("\nEnter a valid Roman Numerals please....")
        exit()
    elif user[i] == "L" and user[i+1] not in "IVXL":
        print("\nEnter a valid Roman Numerals please....")
        exit()

# Rule 6 ?
if len(user) > 2:
    for i in range(2, n):
        if user[i] == "X" and len([j for j in user[:i-1] if j in "VI"]) > 0:
            print("\nEnter a valid Roman Numerals please....")
            exit()
        elif user[i] == "L" and len([j for j in user[:i-1] if j in "IVX"]) > 0:
            print("\nEnter a valid Roman Numerals please....")
            exit()
        elif user[i] == "C" and len([j for j in user[:i-1] if j in "VXI"]) > 0:
            print("\nEnter a valid Roman Numerals please....")
            exit()
        elif user[i] == "D" and len([j for j in user[:i-1] if j in "VXIC"]) > 0:
            print("\nEnter a valid Roman Numerals please....")
            exit()
        elif user[i] == "M" and len([j for j in user[:i-1] if j in "VXIC"]) > 0:
            print("\nEnter a valid Roman Numerals please....")
            exit()

res = 0
values = [roman_numbers.get(x) for x in user]
n = len(values)

# Converting process (Rule 4 & 5)
for i in range(n-1):
    if values[i] < values[i+1]:
        res -= values[i]
    else:
        res += values[i]
res += values[n-1]
print(res)
exit()
