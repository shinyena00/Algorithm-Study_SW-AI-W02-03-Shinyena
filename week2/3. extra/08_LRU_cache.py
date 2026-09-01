class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value  = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            if node.prev == self.head:
                return node.value
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            if node.prev == self.head:
                return 
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

        else:
            new_node = Node(key, value)
            if len(self.dict) == self.capacity:
                node = self.tail.prev
                del self.dict[node.key]
                node.prev.next = self.tail
                self.tail.prev = node.prev
            
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node

            self.dict[key] = new_node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)