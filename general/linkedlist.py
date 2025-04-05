
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(root):
    if root == None:
        print("List Empty!")
    else:
        while root:
            print(root.val, end="->")
            root = root.next
    print()

def reverse_list(head):
    if head == None:
        return
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ =="__main__":
    head = Node(3)
    head.next = Node(7)
    head.next.next = Node(2)
    head.next.next.next = Node(8)
    
    print_list(head)
    newhead = reverse_list(head)
    print_list(newhead)