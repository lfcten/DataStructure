"""
python string hash:
int len = strObject->length;
unsignedchar * p = (unsignedchar *)strObject->value;
long x = *p << 7;
while (--len >= 0)
    x = (1000003*x) ^ *p++;
x ^= strObject->length;
if (x == -1)
    x = -2;
strObject->hashValue = x;
"""



class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def put_data_in_slot(self,key,data,slot):
        if self.slots[slot] is None:
            self.slots[slot] = key
            self.data[slot] = data
            return True
        elif self.slots[slot] == key:
            self.data[slot] == data
            return True
        else:
            return False

    def put(self,key,data):
        slot = self.hash_function(key,self.size)
        result = self.put_data_in_slot(key,data,slot)
        while not result:
            slot = self.rehash(slot,self.size)
            result = self.put_data_in_slot(key,data,slot)

    # reminder method
    def hash_function(self,key,size):
        return key % size
    # 线性探测处理碰撞
    def rehash(self,old_hash,size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)



if __name__=="__main__":
    table = HashTable()
    table[54] = 'cat'
    table[26] = 'dog'
    table[93] = 'lion'
    table[17] = "tiger"
    table[77] = "bird"
    table[44] = "goat"
    table[55] = "pig"
    table[20] = "chicken"
    print(table.slots)
    print(table.data)


