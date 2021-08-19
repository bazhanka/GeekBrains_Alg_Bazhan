import string

def where_letters(a,b):
    alphabet=string.ascii_lowercase
    try:
        a in alphabet and b in alphabet
        if True:
            inda = alphabet.index(a)+1
            indb = alphabet.index(b)+1
            if inda>indb:
                number=inda-indb - 1
            else:
                number=indb-inda - 1
            return f'{a} - {inda} буква в алфавите, {b} - {indb} буква в алфавите, между ними {number} букв'
    except ValueError:
        return "Функция принимает только буквы латинского алфавита"
print(where_letters('a', 'z'))