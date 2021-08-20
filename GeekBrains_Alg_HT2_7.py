n = int(input("Введите n "))
sum = 0
thesum = int ((n*(n+1))/2)
for el in range (1,n+1):
    sum += el
if sum == thesum:
    print (f'Теорема верна - сумма от 1 до {n} = {sum} и равна n*(n+1))/2 = {thesum}')
else:
    print (f'Теорема неверна - сумма от 1 до {n} = {sum} неравна n*(n+1))/2 = {thesum}')