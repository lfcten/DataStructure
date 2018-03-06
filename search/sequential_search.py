import time
import datetime
def sequential_search(a_list,item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

def sequential_search1(a_list,item):
    for num in a_list:
        if num == item:
            return True
    return False
if __name__ == "__main__":
    test_list = range(1500000000000000)
    print(datetime.datetime.now(), sequential_search(test_list, 1500000), datetime.datetime.now())
    time.sleep(3)
    print(datetime.datetime.now(), sequential_search1(test_list, 150000), datetime.datetime.now())