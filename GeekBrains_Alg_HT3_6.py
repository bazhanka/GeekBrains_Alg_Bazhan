def countint_min_max(*args):
    list = [*args]
    maximum = max(list)
    minimum = min(list)
    sum = 0
    indmax=list.index(maximum)
    indmin=list.index(minimum)
    if indmin < indmax:
        for el in list[indmin+1:indmax]:
            sum+=el
    elif indmax < indmin:
        for el in list[indmax+1:indmin]:
            sum+=el
    return sum

print (countint_min_max(1,2,9,3,4,4,6,1,9))