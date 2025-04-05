
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    


class FreqList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_head(self, key):
        node = ListNode(key)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        return node
    
    def remove_node(self, node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    def is_empty(self):
        return self.head.next == self.tail

class AllOne:
    def __init__(self):
        self.key_map = {}
        self.freq_map = {}
        self.max_freq = 0
        self.min_freq = 0
    
    def inc(self, key):
        if key not in self.key_map:
            freq = 1
            if freq not in self.freq_map:
                self.freq_map[freq] = FreqList()
            node = self.freq_map[freq].add_to_head(key)
            self.key_map[key] = (freq, node)
            self.min_freq = freq
            self.max_freq = max(self.max_freq, 1)
        else:
            freq, node = self.key_map[key]
            self.freq_map[freq].remove_node(node)
            if self.freq_map[freq].is_empty():
                del self.freq_map[freq]
                if self.min_freq == freq:
                    self.min_freq = freq + 1
            if freq + 1 not in self.freq_map:
                self.freq_map[freq + 1] = FreqList()
            new_node = self.freq_map[freq+1].add_to_head(key)
            self.key_map[key] = (freq+1, new_node)
            self.max_freq = max(self.max_freq, 1)
            
            
    
    def dec(self, key):
        pass
    
    def getMaxKey(self):
        pass
    
    def getMinKey(self):
        pass