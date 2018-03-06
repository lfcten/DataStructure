import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j//(radix**(i-1)) % (radix)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

import random
def radixSort1():
    A=[random.randint(1,99) for i in range(10000)]
    for k in range(2):
        s=[[] for i in range(10)]
        for i in A:
            s[i//(10**k)%10].append(i)
        A=[a for b in s for a in b]
    return A
a =  radixSort1()
b = radix_sort([1,1112,113,2,13,25,23,17,22])
print(b)
