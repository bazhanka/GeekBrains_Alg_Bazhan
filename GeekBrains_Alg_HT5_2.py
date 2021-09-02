from collections import deque
d={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def my_hex(a):
    hexa=[]
    if a//16 !=0:
        while a//16 != 0:
            hexa.append(d[(a%16)])
            a=a//16
            if a//16 == 0:
                hexa.append(d[(a%16)])
                break
    elif a // 16 == 0:
        hexa.append(d[(a % 16)])
    return hexa

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def sum_hex(a,b):
    #принимает два числа в десятичной системе
    hexa = my_hex(a)
    hexb = my_hex(b)
    sumx = []
    index = 0
    plus = 0
    while index < len(hexa) or index < len(hexb):
        try:
            inta = get_key(d,hexa[index])
            intb = get_key(d,hexb[index])
            sum = inta+intb+plus
            index+=1
            if sum < 16:
                sumx.append(d[sum])
                plus = 0
            else:
                n = sum - 16
                sumx.append(d[n])
                plus = 1
        except IndexError:
            if index == len(hexb):
                a = get_key(d,hexa[index])+plus
                sumx.append(d[a])
                index+=1
                plus = 0
            else:
                b = get_key(d,hexb[index])+plus
                sumx.append(d[b])
                index+=1
                plus = 0
    if plus == 1:
        sumx.append(plus)
    return sumx[::-1]

#print(sum_hex(34002,4563822))
#print(my_hex(34002), hex(34002), my_hex(4563822), hex(4563822))

def mult_hex(a,b):
    #передаются два числа в шеснадцатиричной системе
    if len(a) > len(b):
        l = a
        a = b [::-1]
        b = l [::-1]
    else:
        a = a[::-1]
        b = b[::-1]

    hexa = []
    for el in a:
        try:
            elx = int(el)
            hexa.append(elx)
        except ValueError:
            hexa.append(el.upper())
    hexb = []
    for el in b:
        try:
            elx = int(el)
            hexb.append(elx)
        except ValueError:
            hexb.append(el.upper())
    multx = []
    plus = 0
    for a in hexa:
        inta = get_key(d,a)
        mult1=[]
        for b in hexb:
            intb = get_key(d,b)
            mult = inta*intb+plus
            if mult < 10:
               mult1.insert(0,mult)
               plus = 0
            else:
               mult1.insert(0,mult%16)
               plus = mult//16
        mult1.insert(0,plus)
        multx.append(mult1)
    listys = []
    for listx in multx:
        counter = 0
        while counter < multx.index(listx):
            listx.append(0)
            counter+=1
        listy = listx[::-1]
        listys.append(listy)
    for listy in listys:
        while len(listy) < len(listys[-1]):
            listy.append(0)
    index = 0
    result = []
    plus = 0
    while index < len(listy):
        sum = 0
        for listy in listys:
            sum += listy[index]
        if sum + plus < 16:
            result.append(d[sum+plus])
            plus = 0
            index+=1
        else:
            n = sum + plus - 16
            result.append(d[n])
            plus = 1
            index+=1
    return result[::-1]


    return listys


print(mult_hex('20a4','b15'))