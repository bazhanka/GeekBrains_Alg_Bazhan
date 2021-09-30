import random

list = [random.randint(0,50) for el in range(10)]
print(list)


def merge_line(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    k = start
    l = 0
    r = 0
    while start + l < mid and mid + r < end:
        if left[l] < right[r]:
            list[k] = left[l]
            l += 1
            k +=1
        else:
            list[k] = right[r]
            r += 1
            k += 1
    if start + l < mid:
        while k < end:
            list[k] = left[l]
            l += 1
            k += 1
    else:
        while k < end:
            list[k] = right[r]
            r += 1
            k += 1
    return list

def merge_sort(list,start,end):
    if end - start > 1:
        mid = (start+end)//2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge_line(list, start, mid, end)
    return list

list1 = [6,7,10,2,4,5]
print(merge_sort(list,0,10))
#print(cool_sort(list))
