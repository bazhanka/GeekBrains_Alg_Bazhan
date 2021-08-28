import timeit
import cProfile

def divisible(start,stop):
    d={}
    for a in range(start, stop):
        for num in range (2,10):
            if a % num == 0:
                if num not in d.keys():
                    d[num] = []
                    d[num] += [a]
                else:
                    d[num] += [a]
    return f'В диапазоне {start} - {stop-1} кратны: {d}'

#print (divisible(2,100))

print(timeit.timeit('d={}')) #0.016576000000000004
print(cProfile.run("divisible(2,10000)")) #18288 function calls in 0.008 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#        1    0.007    0.007    0.008    0.008 GeekBrains_Alg_HT3_1.py:4(divisible)
#        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    18284    0.001    0.000    0.001    0.000 {method 'keys' of 'dict' objects}

def div_damir(pos):
    d = {}
    for i in range (2,10):
        counter = 0
        for j in range(i,pos,i):
            if j < pos:
                counter += 1
        d.update({i:counter})
    return d
#print(div_damir(10000))
print(timeit.timeit('d={}')) #0.013204499999999997
print(cProfile.run('div_damir(10000)')) #12 function calls in 0.001 seconds

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 GeekBrains_Alg_HT3_1.py:28(div_damir)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        8    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
