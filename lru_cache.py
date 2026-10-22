class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        self.capacity = capacity
        self.cache = {}

        # Dummy nodes simplify insertion and removal.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _mark_recently_used(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._mark_recently_used(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._mark_recently_used(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            # The node before the tail is least recently used.
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)
    print(cache.get(1))  # 10

    cache.put(3, 30)     # Evicts key 2
    print(cache.get(2))  # -1
    print(cache.get(3))  # 30

    cache.put(1, 15)     # Updates key 1
    print(cache.get(1))  # 15
