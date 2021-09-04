#python 3.8
#64-bit

import sys

n = int(input("Введите n ")) #n - 24 бит, согласно встроенной функции - 28 бит
print(sys.getsizeof(n))
sum = 0
thesum = int ((n*(n+1))/2) #thesum - 24 бит, согласно встроенной функции - 28 бит
print(sys.getsizeof(thesum))
for el in range (1,n+1):
    sum += el #sum - 24 бит
if sum == thesum:
    print (f'Теорема верна - сумма от 1 до {n} = {sum} и равна n*(n+1))/2 = {thesum}')
else:
    print (f'Теорема неверна - сумма от 1 до {n} = {sum} неравна n*(n+1))/2 = {thesum}')



import string

def where_letters(a,b):
    alphabet = '' #пустой alphabet согласно встроенной функции - 49 бит
    print(sys.getsizeof(alphabet))
    alphabet=string.ascii_lowercase #alphabet - 37+26 бит = 63 бит, согласно встроенной функции - 75 бит (49+26)
    alt_alphabet = []
    print(sys.getsizeof(alt_alphabet))
    alt_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(sys.getsizeof(alt_alphabet))
    # эффективнее, чем потенциальный список - 40 + 8*26 = 248 бит, согласно встроенной функции - 264 бит (56+26*8)
    print(sys.getsizeof(alphabet))
    try:
        a in alphabet and b in alphabet
        if True:
            inda = alphabet.index(a)+1 #inda - 24 бит, согласно встроенной функции - 28 бит
            print(sys.getsizeof(inda))
            indb = alphabet.index(b)+1 # indb - 24 бит, согласно встроенной функции - 28 бит
            print(sys.getsizeof(indb))
            if inda>indb:
                number=inda-indb - 1 #number - 24 бит
                print(sys.getsizeof(number))
            else:
                number=indb-inda - 1 #number  - 24 бит
                print(sys.getsizeof(number))
            return f'{a} - {inda} буква в алфавите, {b} - {indb} буква в алфавите, между ними {number} букв'
    except ValueError:
        return "Функция принимает только буквы латинского алфавита"
print(where_letters('a', 'z'))



def divisible(start,stop):
    d={} #пустой словарь, согласно встроенной функции - 64 бит
    print(sys.getsizeof(d))
    #248+24*8 (сам словарь - 440 бит)+ 24*8 (ключи - 192 бит) + 8(40 + 8*n + 24*n), где n - число эл-тов в каждом списке значений словаря (8 раз с разными n)
    #согласно встроенной функции - 360 бит
    for a in range(start, stop+1):
        for num in range (2,10):
            if a % num == 0:
                if num not in d.keys():
                    d[num] = []
                    d[num] += [a]
                else:
                    d[num] += [a]
    print(sys.getsizeof(d))
    print(sys.getsizeof(d.keys()))
    print(sys.getsizeof(d.values()))
    return f'В диапазоне {start} - {stop-1} кратны: {d}'

print (divisible(2,100))