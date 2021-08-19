def year(a):
    if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
        return "Год невисокосный"
    else:
        return "Год високосный"

print (year(2020))