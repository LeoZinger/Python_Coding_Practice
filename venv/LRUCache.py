class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_q = [] * capacity
        self.lru_dict = {}

    def get(self, key: int) -> int:
        if key in self.lru_dict:
            self.lru_q.remove(key)
            self.lru_q.append(key)
            return self.lru_dict.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dict:
            self.lru_q.remove(key)
            self.lru_q.append(key)
        else:
            self.lru_q.append(key)
        self.lru_dict[key] = value

        if len(self.lru_q) > self.capacity:
            evict_key = self.lru_q.pop(0)
            self.lru_dict.pop(evict_key)


# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# lRUCache = LRUCache(2)
# print(lRUCache.__dict__)
# print("put 1, 1 ")
# lRUCache.put(1, 1); # cache is {1=1}
# print("put 2, 2 ")
# lRUCache.put(2, 2); # cache is {1=1, 2=2}
# print(lRUCache.__dict__)
# res = lRUCache.get(1)
# print(res)  # return 1
# print("put 3, 3 ")
# lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print("get 2: ", lRUCache.get(2));    # returns -1 (not found)
# print("put 4, 4 ")
# lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.__dict__)
# print("get 1: ", lRUCache.get(1));    # return -1 (not found)
# print("get 3: ", lRUCache.get(3));    # return 3
# print("get 4: ", lRUCache.get(4));    # return 4
# print("put 2")
# lRUCache.put(2, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print("get 2: ", lRUCache.get(2)); # returns 2

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
lRUCache = LRUCache(2)
print(lRUCache.__dict__)
print("put 2, 1 ")
lRUCache.put(2, 1); # cache is {1=1}
print("put 2, 2 ")
lRUCache.put(2, 2); # cache is {1=1, 2=2}
print(lRUCache.__dict__)
print("get 2: ", lRUCache.get(2));    # returns -1 (not found)
print("put 1, 1 ")
lRUCache.put(1, 1); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.__dict__)
print("put 4, 1 ")
lRUCache.put(4, 1); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.__dict__)
print("get 2: ", lRUCache.get(2));    # return -1 (not found)
