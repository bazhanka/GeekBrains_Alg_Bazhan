import random

list = [random.randint(-100,100) for el in range(10)]
print(list)
def bubble_sort(list):
    n = 1
    while n < len(list):
        for ind in range (len(list)-n):
            if list[ind] < list[ind+1]:
                list[ind], list[ind+1] = list[ind+1], list[ind]
        n+=1
    return list
print(bubble_sort(list))