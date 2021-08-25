def change_min_max(*args):
    list = [*args]
    maximum = max(list)
    minimum = min(list)
    list[list.index(maximum)] = minimum
    list[list.index(minimum)] = maximum
    return list

print (change_min_max(1,2,3,4,5,6,7,8,9))