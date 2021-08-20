n = int(input('Введите длину ряда'))
el = 1
sum = 1
count = 0
while count < n-1:
    el = el*-0.5
    print (el)
    sum += el
    count += 1
print(sum)