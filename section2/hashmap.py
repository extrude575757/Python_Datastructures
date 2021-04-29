class HashMap:
    def __init__(self):
        self.max_length = 8
        self.max_load_factor = 0.8
        self.length = 0
        self.map = [None] * self.max_length
        self.keyslist = []

    
    def get(self, key, default=None):

        if self.map[key] is not None:
            for pair in self.map[key]:
                if pair[0] == key:
                    return pair[1]
        else:
            return None
        # returns the value for key if key is in the dictionary, else default. If default is not given, it defaults to none.

    def set(self, key, value):
        key_value = [key, value]
        self.keyslist.append(key)
        if self.map[key] is None:
            self.map[key] = list([key_value])
            if self.max_load_factor >= .8:
                self.rehash(self.capacity * 2)
            return True
        else:
            for pair in self.map[key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key].append(key_value)
            if self.max_load_factor >= .8:
                self.rehash(self.capacity * 2)
            return True

        # set the (key,value) pair to the hashMap. After seting, if the load-factor >= 80%, rehash the map into a map double its current capacity

    def clear(self):
        self.map.clear()
        # empty the hashmap

    def capacity(self):
        return self.max_length  # return the current capacity -- number of buckets-- in the map

    def size(self):
        return self.length
        

    def keys(self):
        return self.keyslist  # return a list of keys

    def rehash(self):
        self.map = [None] * (self.max_length * 2)
        return self.map
