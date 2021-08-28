import cProfile
import math
def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number

def simple_num(n):
    p = prime_counting_function(n)
    a = [0] * p
    for i in range(p):
        a[i] = i
        a[1] = 0
    m = 2
    while m < p:
        if a[m] != 0:
            j = m * 2
            while j < p:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b[n-1]
print(simple_num(100))
print(cProfile.run('simple_num(100000)')) #1524609 function calls in 0.672 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.004    0.004    0.672    0.672 <string>:1(<module>)
#        1    0.376    0.376    0.668    0.668 GeekBrains_Alg_HT4_2.py:11(simple_num)
#        1    0.186    0.186    0.287    0.287 GeekBrains_Alg_HT4_2.py:3(prime_counting_function)
#        1    0.000    0.000    0.672    0.672 {built-in method builtins.exec}
#  1416360    0.102    0.000    0.102    0.000 {built-in method math.log}
#   108244    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def simple_dimple(n):
    p = prime_counting_function(n)
    a=[el for el in range (3,p)]
    simple=[2]
    for el in a:
        for sim in simple:
            if el % sim == 0:
                el = 0
            else:
                if sim == simple[-1]:
                    simple.append(el)
    return simple[n-1]

print(simple_dimple(100))
print(cProfile.run('simple_dimple(10000)')) #127691 function calls in 19.414 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001   19.413   19.413 <string>:1(<module>)
#        1    0.015    0.015    0.023    0.023 GeekBrains_Alg_HT4_2.py:3(prime_counting_function)
#        1   19.386   19.386   19.413   19.413 GeekBrains_Alg_HT4_2.py:42(simple_dimple)
#        1    0.003    0.003    0.003    0.003 GeekBrains_Alg_HT4_2.py:44(<listcomp>)
#        1    0.000    0.000   19.414   19.414 {built-in method builtins.exec}
#   116671    0.008    0.000    0.008    0.000 {built-in method math.log}
#    11014    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def frominet(n): #позаимствовано из сети для сравнения производительности
    p=prime_counting_function(n)
    lst=[2]
    for i in range(3, p+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[n-1]

print(frominet(100))
print(cProfile.run('frominet(100000)')) #1524608 function calls in 1.536 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    1.536    1.536 <string>:1(<module>)
#        1    0.186    0.186    0.290    0.290 GeekBrains_Alg_HT4_2.py:3(prime_counting_function)
#        1    1.241    1.241    1.536    1.536 GeekBrains_Alg_HT4_2.py:68(frominet)
#        1    0.000    0.000    1.536    1.536 {built-in method builtins.exec}
#  1416360    0.104    0.000    0.104    0.000 {built-in method math.log}
#   108243    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}