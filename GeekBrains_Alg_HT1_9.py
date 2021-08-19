def middle(a,b,c):
    if a<b<c or c<b<a:
        return f"Среднее число - {b}"
    elif b<a<c or c<a<b:
        return f"Среднее число - {a}"
    elif b<c<a or a<c<b:
        return f"Среднее число - {c}"
    else:
        return "Нет среднего числа"

print(middle(2,3,4))
print(middle(2,1,4))
print(middle(2,1,1))
