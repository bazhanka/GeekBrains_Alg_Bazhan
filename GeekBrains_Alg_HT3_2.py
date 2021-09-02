def count_mass(*args):
    mass = (args)
    ind=[]
    for el in mass:
        if el % 2 == 0:
            ind.append(mass.index(el))
    return ind
print (count_mass(1,2,3,4,5,6))