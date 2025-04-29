from collections import deque
class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.data = deque()
        self.total = 0
    
    def next(self, val) -> float:
        self.total += val
        self.data.append(val)
        if len(self.data) > self.size:
            prev = self.data.popleft()
            self.total -= prev
        return self.total / len(self.data)