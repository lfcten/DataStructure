import datetime
import time
def binary_search(a_list,item):
    low = 0
    high = len(a_list) - 1
    while low <= high:
        mid = low + ((high-low)>>2)
        if a_list[mid] == item:
            return True
        elif a_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search1(a_list,item):
    mid = len(a_list)//2
    while a_list:
        if a_list[mid] == item:
            return True
        elif a_list[mid] > item:
            return binary_search(a_list[:mid],item)
        else:
            return binary_search(a_list[mid+1:],item)
    return False





if __name__ == "__main__":
    test_list = range(1500000000000000)
    print(datetime.datetime.now(),binary_search(test_list, 15000000000000),datetime.datetime.now())
    time.sleep(3)
    print(datetime.datetime.now(),binary_search1(test_list,150000000000000),datetime.datetime.now())