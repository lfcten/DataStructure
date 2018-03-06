#稳定排序

def bubble_sort(a_list):
    length = len(a_list)
    while length:
        for i in range(length-1):
            if a_list[i] > a_list[i+1]:
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
        length -= 1

def bubble_sort1(a_list):
    length = len(a_list)
    exchage = True
    while length and exchage:
        exchage = False
        for i in range(length-1):
            if a_list[i] > a_list[i+1]:
                exchage = True
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
        length -= 1

if __name__=="__main__":
    a_list = [20,40,30,30,90,50,80]
    bubble_sort(a_list)
    print(a_list)


