from collections import defaultdict

def counting_sort(A):
    B, C = [], defaultdict(list)  # Output and "counts"
    for x in A:
        C[x].append(x)  # "Count" key(x)
        print(C)
    for k in range(min(C), max(C) + 1):  # For every key in the range
        B.extend(C[k])  # Add values in sorted order
    return B

