def sumroot(root):
    def dfs(node, curr_val):
        if not node:
            return 0
        curr_val = curr_val * 10 + node.val
        
        if not node.left and not node.right:
            return curr_val
        
        return dfs(node.left, curr_val) + dfs(node.right, curr_val)
    
    return dfs(root, 0)