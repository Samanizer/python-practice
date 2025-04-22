from collections import deque, defaultdict
class TreeNode:
    ...

def rightsideview(root: TreeNode) -> list[int]:
    result = []
    que = deque([(root, 0)])
    lmap = defaultdict(list)
    
    while que:
        node, level = que.popleft()
        lmap[level].append(node.val)
        
        if node.left:
            que.append((node.left, level + 1))
        if node.right:
            que.append((node.right, level + 1))
    
    for ls in lmap.values():
        result.append(ls[-1])
    
    return result

def right_view_2(root: TreeNode) -> list:
    result = []
    que = deque([root])
    
    while que:
        level_len = len(que)
        for i in range(level_len):
            node = que.popleft()
            
            if i == level_len - 1:
                result.append(node.val)
            
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
    
    return result
        