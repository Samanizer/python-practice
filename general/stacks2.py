class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, i):
        self.data.append(i)
    
    def pop(self):
        return self.data.pop() if self.data else None
    
    def peek(self):
        return self.data[len(self.data) - 1] if self.data else None
    
    def __repr__(self):
        return "Stack: " + str(self.data)
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.peek())
    print(s.pop())
    print(s)
    s.pop()
    s.pop()
    s.peek()
    s.pop()