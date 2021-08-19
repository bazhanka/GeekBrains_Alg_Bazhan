def fun_func(a):
    a=str(a)
    add=1
    summa=0
    for el in a:
        add=int(el)*add
        summa+=int(el)
    return f'Сумма цифр: {summa}, Произведение цифр: {add}'

print (fun_func(345))