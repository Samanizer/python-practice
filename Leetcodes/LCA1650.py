class TreeNode:
    ...

def LCA(p: TreeNode, q: TreeNode) -> TreeNode:
    ancestors = set()
    
    node = p
    while node:
        ancestors.add(node)
        node = node.parent
    
    node = q
    while node:
        if node in ancestors:
            return node
        node = node.parent
    
    return None