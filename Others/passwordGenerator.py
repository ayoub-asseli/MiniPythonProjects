import string
from random import randint

#Generateur de mot de passe à 15 caractères
letter_lower = string.ascii_lowercase
letter_upper = string.ascii_uppercase
numbers = list(range(0, 10))
ch_special = "#&!+?;:,°-_*$£%=^'"
generator = [letter_lower, letter_upper, numbers, ch_special]
password = ""
for i in range(0, 15):
    a = randint(0, 3)
    b = randint(0, len(generator[a])-1)
    password += str(generator[a][b])
print(password)
