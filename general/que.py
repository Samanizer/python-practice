class Que:
    def __init__(self):
        self.data = []
    
    def enque(self, i):
        self.data.append(i)
    
    def deque(self):
        return self.data[0] if self.data else None
    
        