# 稳定排序
# O(n^2) 移位操作耗时较大

def insert_sort(a_list):
    for i in range(1,len(a_list)):
        current_val = a_list[i]
        while i and a_list[i-1] > current_val:
            if a_list[i-1] > current_val:
                a_list[i] = a_list[i-1]
            i -= 1
        a_list[i] = current_val

def insert_sort_binarysearch(a_list):
    for i in range(1,len(a_list)):
        current_val = a_list[i]
        if a_list[i-1] > current_val:
            low = 0
            high = i - 1
            while low < high :
                mid = low + (high - low)//2
                if a_list[mid] > current_val:
                    high = mid
                else:
                    low = mid + 1
            while i > low:
                a_list[i] = a_list[i-1]
                i -= 1
        a_list[i] = current_val




if __name__=='__main__':
    a_list = [1,2,3,2,54, 26, 27,28,93, 15, 77, 31, 44, 55, 20]
    insert_sort(a_list)
    print(a_list)
    a_list = [1, 2,2, 3, 54, 26, 27, 28, 93, 15, 77, 31, 44, 55, 20]
    insert_sort_binarysearch(a_list)
    print(a_list)