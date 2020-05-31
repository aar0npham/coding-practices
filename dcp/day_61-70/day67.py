'''
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the
    least frequently used item. If there is a tie, then the least recently used key should be removed.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''


class CacheNode:
    '''double linked list'''

    def __init__(self, key, value, freq_node, prev, next):
        self.key = key
        self.value = value
        self.freq_node = freq_node
        self.prev = prev
        self.next = next

    def free(self):
        if self.freq_node.cache_head == self.freq_node.cache_tail:
            self.freq_node.cache_head = self.freq_node.cache_tail = None
        elif self.freq_node.cache_head == self:
            self.next.prev = None
            self.freq_node.cache_head = self.next
        elif self.freq_node.cache_tail == self:
            self.prev.next = None
            self.freq_node.cache_tail = self.prev
        else:
            self.prev.next = self.next
            self.next.prev = self.prev
        self.prev = None
        self.next = None
        self.freq_node = None


class FreqNode:
    def __init__(self, freq, prev, next):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.cache_head = None
        self.cache_tail = None

    def count_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return 0
        elif self.cache_head == self.cache_tail:
            return 1
        else:
            return '2+'

    def remove(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        prev = self.prev
        next = self.next
        self.prev = self.next = self.cache_head = self.cache_tail = None

        return (prev, next)

    def pop_head_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return None
        elif self.cache_head == self.cache_tail:
            cache_head = self.cache_head
            self.cache_head = self.cache_tail = None
            return cache_head
        else:
            cache_head = self.cache_head
            self.cache_head.next.prev = None
            self.cache_head = self.cache_head.next
            return cache_head

    def append_cache_to_tail(self, cache_node):
        cache_node.freq_node = self

        if self.cache_head is None and self.cache_tail is None:
            self.cache_head = self.cache_tail = cache_node
        else:
            cache_node.prev = self.cache_tail
            cache_node.next = None
            self.cache_tail.next = cache_node
            self.cache_tail = cache_node

    def insert_after(self, freq_node):
        freq_node.prev = self
        freq_node.next = self.next

        if self.next is not None:
            self.next.prev = freq_node

        self.next = freq_node

    def insert_before(self, freq_node):
        if self.prev is not None:
            self.prev.next = freq_node

        freq_node.prev = self.prev
        freq_node.next = self
        self.prev = freq_node


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq = None
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            c_node = self.cache[key]
            freq_node = c_node.freq_node
            value = c_node.value
            self.move_forward(c_node, freq_node)

            return value
        else:
            return -1

    def set(self, key, value):
        if self.capacity <= 0:
            return -1

        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.dump_cache()
            self.create_cache(key, value)
        else:
            c_node = self.cache[key]
            freq_node = c_node.freq_node
            value = c_node.value
            self.move_forward(c_node, freq_node)

    def move_forward(self, cache_node, freq_node):
        if freq_node.next is None or freq_node.next.freq != freq_node.freq + 1:
            target_freq_node = FreqNode(freq_node.freq + 1, None, None)
            target_empty = True
        else:
            target_freq_node = freq_node.next
            target_empty = False

        cache_node.free()
        target_freq_node.append_cache_to_tail(cache_node)

        if target_empty:
            freq_node.insert_after(target_freq_node)

        if freq_node.count_cache() == 0:
            if self.freq == freq_node:
                self.freq = target_freq_node

            freq_node.remove()

    def dump_cache(self):
        head_freq_node = self.freq
        self.cache.pop(head_freq_node.cache_head.key)
        head_freq_node.pop_head_cache()

        if head_freq_node.count_cache() == 0:
            self.freq = head_freq_node.next
            head_freq_node.remove()

    def create_cache(self, key, value):
        cache_node = CacheNode(key, value, None, None, None)
        self.cache[key] = cache_node

        if self.freq is None or self.freq.freq != 0:
            new_freq_node = FreqNode(0, None, None)
            new_freq_node.append_cache_to_tail(cache_node)

            if self.freq is not None:
                self.freq.insert_before(new_freq_node)

            self.freq = new_freq_node
        else:
            self.freq.append_cache_to_tail(cache_node)


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.get(1)
    cache.set(3, 3)
    cache.get(2)
    cache.get(3)
    cache.set(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
