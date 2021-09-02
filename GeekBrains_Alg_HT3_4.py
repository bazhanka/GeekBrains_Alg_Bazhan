def count_els(*args):
    list=[*args]
    num = 0
    elem = ''
    for el in args:
        newnum = list.count(el)
        if newnum > num:
            num = newnum
            elem = el
    return f'Наибольшее число вхождений цифры {elem} - {num} раз'

print(count_els(1,2,2,2,3,4,4,4,6,6,62,2,3))