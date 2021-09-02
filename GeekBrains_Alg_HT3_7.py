def findmin(*args):
    list = [*args]
    minimum1 = min(list)
    list.remove(minimum1)
    minimum2 = min(list)
    return minimum1 , minimum2

print(findmin(1,2,3,4,6,1))