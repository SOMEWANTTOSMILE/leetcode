class MyHashMap:
    def __init__(self):
        self.hashmap_list = list()
        self.key = None
        self.value = None

    def put(self, key, value):
        for i in self.hashmap_list:
            if [i[0] and i[1]] == [key, value]:
                return
        self.key = key
        self.value = value
        list_put = [key, value]
        self.hashmap_list.append(list_put)

    def get(self, key):
        self.key = key
        for i in self.hashmap_list:
            if i[0] == key:
                print(i[1])
                break
            elif i[0] != key:
                print(-1)
                break

    def remove(self, key):
        self.key = key
        for i in self.hashmap_list:
            if i[0] == key:
                self.hashmap_list.remove(i)


list_key_value = MyHashMap()
list_key_value.put(1, 2)
list_key_value.put(3, 3)
print(list_key_value.hashmap_list)
list_key_value.get(4)
list_key_value.remove(1)
print(list_key_value.hashmap_list)
