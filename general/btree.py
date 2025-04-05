from collections import deque

class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def PreOrder(root):
    if root == None:
        return
    print(root.val, end=" -> ")
    PreOrder(root.left)
    PreOrder(root.right)

def InOrder(root):
    if root == None:
        return
    InOrder(root.left)
    print(root.val, end=" -> ")
    InOrder(root.right)

def PostOrder(root):
    if root == None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.val, end=" -> ")
    
def LevelTraversal(root):
    if root == None:
        return
    que = deque()
    m = {}
    que.append((root, 0))
    while que:
        node, level = que.popleft()
        m.setdefault(level,[]).append(node.val)
        if node.left:
            que.append((node.left, level+1))
        if node.right:
            que.append((node.right, level+1))
    for level in sorted(m.keys()):
        print("Level: ", level, m[level])

def VerticalLevels(root):
    m = {}
    que = deque()
    que.append((root, 0, 0))
    while que:
        node, hd, level = que.popleft()
        m.setdefault(hd,[]).append(node.val)
        if node.left:
            que.append((node.left, hd - 1, level + 1))
        if node.right:
            que.append((node.right, hd + 1, level + 1))
    for key in sorted(m.keys()):
        print("HD:", key, m[key])
        


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("PreOrder")
    PreOrder(root)
    print("")
    print("InOrder")
    InOrder(root)
    print("")
    print("PostOrder")
    PostOrder(root)
    print("")
    print("LevelTraversal")
    LevelTraversal(root)
    print("")
    print("VerticalTraversal")
    VerticalLevels(root)
    print("")