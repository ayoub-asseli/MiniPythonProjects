"""
Your function should convert the number to a string and add commas as a thousands 
separator.
"""

def format_number(number):
	number, new_number, i = str(number), '', 0
	if len(number) <= 3:
		return number
	else:
		for index in range(len(number)-1,-1, -1):
			new_number += number[index]
			i += 1
			if i == 3:
				new_number += ','
				i = 0
	new_number = new_number[::-1]
	if new_number[0] == ',':
		new_number = new_number[1:]
	return new_number
