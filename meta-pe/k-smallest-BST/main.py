'''
Given the root of a Binary Search Tree (BST) and an integer k,
return the k-th smallest element in the BST.
'''

def kth_smallest(root, k):
    count = 0
    result = None
    
    def inorder(node):
        nonlocal count, result
        
        if not node or result is not None:
            return
        
        inorder(node.left)
        count += 1
        if count == k:
            result = count
            return
        
        inorder(node.right)
        
    inorder(root)
    return result    
    