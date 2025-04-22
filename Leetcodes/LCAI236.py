class TreeNode:
    ...
    
def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
    def dfs(node):
        nonlocal p, q
        if not node:
            return None
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if node == p or node == q:
            return node
        
        if left and right:
            return node
        
        return left or right
    
    return dfs(root)