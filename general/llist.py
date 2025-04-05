class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

def reverse(head: Node):
    

head = Node(4)
head.next = Node(6)
head.next.next = Node(10)

curr = head
while curr:
    print(curr.value)
    curr = curr.next

