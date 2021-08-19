def func(x1,y1,x2,y2):
    l=x1-x2
    m=y1-y2
    if l==0:
        return f'Прямая параллельна ОY, x={x1}'
    elif m==0:
        return f'Прямая параллельна ОX, y={y1}'
    else:
        k=m/l
        b=y1-((m*x1)/l)
        return (f'y = {k}x + {b}')

print (func(5,5,12,5))