"""
For the purpose of this challenge, shadow sentences are sentences where every 
word is the same length and order but without any of the same letters. 
Write a function that accepts two parameters that may or may not be shadows of each other. 
The function should return True if they are and False if they aren’t.
An example would be "they are round" and "fold two times," which are shadow sentences, 
while "his friends" and "our company" are not because both contain an r.
"""

def shadow_sentences(sentence1, sentence2):
	for elem1, elem2 in zip(sentence1.split(), sentence2.split()):
		if len(elem1) != len(elem2) or len([value for value in elem1 if value in elem2]) > 0:
			return False
	return True

sentence_1 = "they are round"
sentence_2 = "fold two times"
print(shadow_sentences(sentence_1, sentence_2))
