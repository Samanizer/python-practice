import random

class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class DList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, key, val):
        node = ListNode(key, val)
        temp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        temp.next = node
        node.prev = temp
        return node
    
    def remove_node(self,node):
        if node == self.head or node == self.tail:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
    def remove_head(self):
        if self.head.next != self.tail:
            node = self.head.next
            node.next.prev = self.head
            self.head.next = node.next
            return node
        else:
            return None
    
    def print(self):
        print("head <->", end=" ")
        node = self.head.next
        while node != self.tail:
            print(node.val, end=" ")
            print("<->", end=" ")
            node = node.next
        print("tail")
    
    def print_reverse(self):
        print("tail <->", end=" ")
        node = self.tail.prev
        while node != self.head:
            print(node.val, end=" ")
            print("<->", end=" ")
            node = node.prev
        print("head")


class LRUCache:
    def __init__(self, cap):
        self.map = {}
        self.dlist = DList()
        self.capacity = cap
    
    def get(self,key):
        if key in self.map:
            node = self.map[key]
            self.dlist.remove_node(node)
            new_node = self.dlist.add(node.key, node.val)
            self.map[key] = new_node
            return new_node.val
        return -1
    
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            self.dlist.remove_node(node)
            new_node = self.dlist.add(key, value)
            self.map[key] = new_node
            return
        if len(self.map) >= self.capacity:
            evicted = self.dlist.remove_head()
            del self.map[evicted.key]
        node = self.dlist.add(key, value)
        self.map[key] = node
        return
    


new_list = DList()
for i in range(10):
    r = random.randint(0,10)
    new_list.add(r)
    

new_list.print()
new_list.print_reverse()