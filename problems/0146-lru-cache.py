import collections
import unittest


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = collections.OrderedDict()

    def get(self, key: int) -> int:
        value = self.store.get(key)
        if value is None:
            return -1
        self.store.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.store.get(key) is None and len(self.store) == self.capacity:
            self.store.popitem(False)
        if key in self.store:
            self.store.move_to_end(key)
        self.store[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        cache = LRUCache(2)
        cache.put(1, 1)     # cache is {1=1}
        cache.put(2, 2)     # cache is {1=1, 2=2}
        data = cache.get(1)    # return 1
        self.assertEqual(data, 1)
        cache.put(3, 3)     # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        data = cache.get(2)    # returns -1 (not found)
        self.assertEqual(data, -1)
        cache.put(4, 4)     # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        data = cache.get(1)    # return -1 (not found)
        self.assertEqual(data, -1)
        data = cache.get(3)    # return 3
        self.assertEqual(data, 3)
        data = cache.get(4)    # return 4
        self.assertEqual(data, 4)

    def test_repeated_keys(self):
        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(1, 1)
        cache.put(2, 3)
        cache.put(4, 1)
        data = cache.get(1)
        self.assertEqual(data, -1)
        data = cache.get(2)
        self.assertEqual(data, 3)

    def test_dont_remove_if_full_and_replacing_key(self):
        cache = LRUCache(2)
        data = cache.get(2)
        self.assertEqual(data, -1)
        cache.put(2, 6)
        data = cache.get(1)
        self.assertEqual(data, -1)
        cache.put(1, 5)
        cache.put(1, 2)
        data = cache.get(1)
        self.assertEqual(data, 2)
        data = cache.get(2)
        self.assertEqual(data, 6)


if __name__ == '__main__':
    unittest.main()
