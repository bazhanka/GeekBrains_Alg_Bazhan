def triangle(a,b,c):
    if a+b<c or b+c<a or a+c<b:
        if a==b or b==c or c==a:
            return "Треугольник равнобедренный"
        elif a==b and b==c:
            return 'Треугольник равносторонний'
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольник не существует"

print(triangle(3,1,1))
