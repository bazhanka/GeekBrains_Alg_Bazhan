a=int(input('Введите целое натуральное число '))
a=str(a)
even=''
not_even=''
for el in a:
    if int(el) % 2 == 0:
        even += el
    else:
        not_even += el
print (f'В числе {a} {len(even)} четных цифр: {even} и {len(not_even)} нечетных цифр: {not_even}')