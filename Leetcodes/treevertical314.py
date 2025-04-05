from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def vertical_traversal(root):
    if root == None:
        return []
    que = deque()
    m = {}
    que.append((root, 0))
    while que:
        node,hd = que.popleft()
        m.setdefault(hd, []).append(node.val)
        if node.left:
            que.append((node.left, hd - 1))
        if node.right:
            que.append((node.right, hd + 1))
    result = []
    for k in sorted(m.keys()):
        result.append(m[k])
    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)

print(vertical_traversal(root))
    