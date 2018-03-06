# 不稳定排序

def select_sort(a_list):
    length = len(a_list)
    while length > 1:
        pos_max = 0
        for i in range(0,length):
            if a_list[i] > a_list[pos_max]:
                pos_max = i
        if pos_max != length-1:
            a_list[pos_max],a_list[length-1]  = a_list[length-1],a_list[pos_max]
        length -= 1


if __name__=="__main__":
    a = [25,26,27,28, 93, 17, 77, 31, 44, 55, 20,93]
    select_sort(a)
    print(a)