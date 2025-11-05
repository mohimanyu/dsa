class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 13) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None

    def keys(self):
        all_keys = []
        for items_arr in self.data_map:
            if items_arr is not None:
                for item in items_arr:
                    all_keys.append(item[0])
        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumbers", 70)
print(my_hash_table.get_item("washers"))

my_hash_table.print_table()

print(my_hash_table.keys())
