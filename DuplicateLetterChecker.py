"""
Create a function in Python that accepts one parameter: a string that’s a sentence. 
This function should return True if any word in that sentence contains duplicate letters 
and False if not.
"""

def duplicate_letter_checker(sentence):
	words = sentence.split()
	for word in words:
		for letter in word.lower():
			if len(word.replace(letter, '')) <= len(word)-2:
				return True
	return False

sentence1 = "Helo World ! What's up?"
sentence2 = "Helo World ! Whata's up?"
print(duplicate_letter_checker(sentence1))
print(duplicate_letter_checker(sentence2))
