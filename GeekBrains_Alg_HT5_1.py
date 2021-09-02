companies = {}
comp = ''
averages = []
while comp != 'q':
    comp = input("Введите q, если закончили. Иначе,введите назавание компании: ")
    if comp == 'q':
        break
    else:
        income = input("Введите прибыль через запятую ").split(',')
        newincome = [int(el) for el in income]
        average = sum(newincome)/(len(newincome))
        averages.append(average)
        companies.update({comp:average})
av_of_av = (sum(averages)/len(averages))
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
morethanav=[]
lessthanav=[]
for value in companies.values():
    if value > av_of_av:
        morethanav.append(get_key(companies,value))
    elif value < av_of_av:
        lessthanav.append(get_key(companies,value))
    else:
        pass
print(f'Компании с доходом выше среднего: {morethanav}\nКомпании с доходом ниже среднего: {lessthanav}')
