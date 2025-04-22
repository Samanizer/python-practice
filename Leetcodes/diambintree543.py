class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxdiameter(root: TreeNode) -> int:
    max_diam = 0
    
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        
        nonlocal max_diam
        max_diam = max(max_diam, left + right)
        
        return 1 + max(left, right)
    
    dfs(root)
    
    return max_diam