
def min_max_matrix(row,col):
    matrix=[]
    countc=0
    minimum=[]
    while countc < col:
        countr=0
        r = []
        while countr < row:
            r.append(int(input('Введите число: ')))
            countr += 1
            if countr == row-1:
                matrix.append(r)
                countc += 1
    index = 0
    while index < col:
        els = []
        for el in matrix:
            els.append(el[index])
        minimum.append(min(els))
        index+=1
    return max(minimum)

print(min_max_matrix(2,2))
