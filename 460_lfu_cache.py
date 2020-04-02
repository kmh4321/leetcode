class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.usage = {}
        self.current = 0
        self.min_freq = 0
        self.last_used_min = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usage[key]+=1
            if self.usage[key] == self.min_freq:
                self.last_used_min.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key] = value
            self.usage[key] += 1
            
        
        if self.current < self.capacity:
            self.cache[key] = value
            self.current += 1
            if key in self.usage:
                self.usage[key] += 1
            else:
                self.usage[key] = 1
            if self.usage[key] == self.min_freq:
                self.last_used_min.append(key)
            if self.usage[key] < self.min_freq:
                self.min_freq = self.usage[key]
                self.last_used_min = []
                self.last_used_min.append(key)
        
        if self.current == self.capactiy and key in self.cache:
            
            to_delete = self.last_used_min.pop(0)
            del(self.cache[to_delete])
            del(self.usage[to_delete])
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
