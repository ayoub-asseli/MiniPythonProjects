string = input("Enter your sentence: ")
list_words = string.split()
acronym = ""
for word in list_words:
    acronym += word[0].upper()
print(acronym)