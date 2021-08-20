sym=''
while sym!='0':
    sym = input('Введите знак арифметического действия ')
    if sym == '0':
        break
    else:
        a= int(input('Введите число '))
        b= int(input('Введите число '))
        if sym == '/':
            try:
                a/b
                if True:
                    print(f'Частное {a} и {b} = {a / b}')
            except ZeroDivisionError:
                print ('На ноль делить нельзя')
            else:
                pass
        elif sym == '*':
            print(f'Произведение {a} и {b} = {a*b}')
        elif sym == '+':
            print (f'Сумма {a} и {b} = {a+b}')
        elif sym == '-':
            print (f'Разность {a} и {b} = {a-b}')
        else:
            print ('Введите /, *, + или -')