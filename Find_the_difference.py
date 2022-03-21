"""
Write a function in Python that accepts two string parameters. The first parameter 
will be a string of characters, and the second parameter will be the same string of 
characters, but they’ll be in a different order and have one extra character. 
The function should return that extra character.

For example, if the first parameter is "eueiieo" and the second is "iieoedue," 
then the function should return "d.
"""

def diff_btw_strings(string1, string2):
	return [elem for elem in string2 if elem not in string1][0]

print(diff_btw_strings("eueiieo", "iieoedue"))
