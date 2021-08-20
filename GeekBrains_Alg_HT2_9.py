def summy(a):
    a=str(a)
    summa=0
    for el in a:
        summa+=int(el)
    return summa
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
listofnums=input("Введите числа: ").split(' ')
sumlist={}
for el in listofnums:
    sumlist[el]=summy(el)
maxel = max(sumlist.values())

print(f'Наибольшая сумма цифр введенных чисел - {maxel} у числа {get_key(sumlist,maxel)}')