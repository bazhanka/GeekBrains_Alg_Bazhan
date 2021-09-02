def funmatrix(row,col):
    matrix=[]
    countc=0
    while countc < col:
        countr=0
        r = []
        while countr < row-1:
            r.append(int(input('Введите число: ')))
            countr += 1
            if countr == row-1:
                r.append(sum(r))
                matrix.append(r)
                countc += 1
    return matrix

print(funmatrix(5,4))