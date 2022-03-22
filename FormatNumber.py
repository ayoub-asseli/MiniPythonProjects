"""
Your function should convert the number to a string and add commas as a thousands 
separator.
"""

def format_number(number):
	number, new_number, i = str(number), '', 0
	for index in range(len(number)-1,-1, -1):
		new_number += number[index]
		i += 1
		if i == 3 and index != 0:
			new_number += ','
			i = 0
	return new_number[::-1]
