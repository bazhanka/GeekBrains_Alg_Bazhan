import random
import string
def randomizer(a,b):
    if a<b:
        alphabet=string.ascii_lowercase
        try:
            a==int(a) and b==int(b)
            if True:
                return random.randrange(a,b)
        except AttributeError:
            pass
        except ValueError:
            pass
        try:
            a in alphabet and b in alphabet
            if True:
                newalphabet=alphabet[alphabet.index(a):alphabet.index(b)]
                return random.choice(newalphabet)
        except TypeError:
            pass
        try:
            a==float(a) and b==float(b)
            if True:
                return random.uniform(a, b)
        except ValueError:
            pass
    else:
        return 'Первое значение должно быть больше второго'

print(randomizer('z','b'))
print(randomizer(5,1))
print(randomizer(7.5,1.2))
print(randomizer(1.5,1.9))
print(randomizer(1,7))
print(randomizer('a','l'))


