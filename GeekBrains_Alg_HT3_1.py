def divisible(start,stop):
    d={}
    for a in range(start, stop):
        for num in range (2,10):
            if a % num == 0:
                if num not in d.keys():
                    d[num] = []
                    d[num] += [a]
                else:
                    d[num] += [a]
    return f'В диапазоне {start} - {stop-1} кратны: {d}'

print (divisible(2,100))