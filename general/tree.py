class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def in_order(node):
    if node == None:
         return
    in_order(node.left)
    print(node.val)
    in_order(node.right)

if __name__ == "__main__":
    root = Node(4,
            left=Node(2, Node(1), Node(3)),
            right=Node(6, Node(5), Node(7))
           )
    in_order(root)
    print()
        
        