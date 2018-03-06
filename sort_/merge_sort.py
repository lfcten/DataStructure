# O(nlogn)
# 稳定排序
def merge_sort(a_list):
    print('splitting ',a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0; j = 0; k = 0;
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
        print("Merging ", a_list)

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def merge_sort1(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort1(lists[:middle])
    right = merge_sort1(lists[middle:])
    return merge(left, right)



if __name__=="__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # merge_sort(a_list)
    # print(a_list)
    print(merge_sort1(a_list))
