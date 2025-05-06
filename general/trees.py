class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    def dfs(node):
        if not node:
            return
        print(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)

def postorder_traversal(root):
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        dfs(node.right)
        print(node.val)
    
    dfs(root)

def root_to_leaf_sum(root):
    total = 0
    def dfs(node, curr_sum):
        if not node:
            return
        nonlocal total
        
        curr_sum += node.val
        
        if not node.left and not node.right:
            total += curr_sum
            return
        
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
    
    dfs(root, 0)
    return total

def root_to_leaf_nums(root):
    total = 0
    def dfs(node, curr_num):
        if not node:
            return
        
        curr_num = curr_num * 10 + node.val
        nonlocal total
        if not node.left and not node.right:
            total += curr_num
            return
        
        dfs(node.left, curr_num)
        dfs(node.right, curr_num)
    
    dfs(root, 0)
    return total


def max_diameter(root):
    max_diam = 0
    def dfs(node):
        nonlocal max_diam
        if not node:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        
        diam = left_depth + right_depth
        max_diam = max(max_diam, diam)
        
        return 1 + max(left_depth, right_depth)

    dfs(root)
    return max_diam
        
def lowest_common_ancestor(root, p, q):
    lca_node = None
    def dfs(node, p, q):
        nonlocal lca_node
        
        if not node:
            return None
        
        if node == p or node == q:
            return node
        
        left = dfs(node.left, p, q)
        right = dfs(node.right, p, q)
        
        if left and right:
           lca_node = node
           return node
        else:
            return left if left else right
    
    dfs(root, p, q)
    return lca_node

def range_sum_bst(root, low, high):
    rsum = 0
    def dfs(node):
        nonlocal rsum
        
        if not node:
            return 0
        
        if node.val < low:
            dfs(node.right)
        elif node.val > high:
            dfs(node.left)
        else:
            rsum += node.val
            dfs(node.left)
            dfs(node.right)
    
    dfs(root)
    return rsum
             
