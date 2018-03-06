class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    def perc_up(self,i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i],self.heap_list[i//2] = self.heap_list[i//2],self.heap_list[i]
            i //= 2

    def insert(self,k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)
    def perc_down(self,i):
        while 2 * i <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i],self.heap_list[mc] = self.heap_list[mc],self.heap_list[i]
            i = mc

    def min_child(self,i):
        if 2 * i + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return  i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val




    def build_heap(self,a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list  = [0] + a_list[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

a_list = [4,1,3,2,16,9,10,14,8,7]
bh = BinHeap()
bh.build_heap(a_list)
print(bh.heap_list)
print(bh.current_size)
bh.insert(10)
bh.insert(7)
print(bh.heap_list)
bh.del_min();
print(bh.heap_list)
print(bh.current_size)