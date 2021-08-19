import string

def what_letter(index):
    if 0 < index < 27:
        alphabet=string.ascii_lowercase
        return alphabet[index-1]
    else:
        return 'В алфавите 26 букв'

print(what_letter(32))