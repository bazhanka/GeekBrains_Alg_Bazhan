from numpy import median
import random
m = 9
list = [random.randint(0,50) for el in range((2*m)+1)]
print(list)
print (median(list))

def my_median(list):
    for cur_el in list:
        count_bigger = 0
        count_less = 0
        for el in list:
            if cur_el > el:
                count_bigger += 1
            elif cur_el < el:
                count_less += 1
        if count_bigger == count_less:
            return cur_el

print(my_median(list))