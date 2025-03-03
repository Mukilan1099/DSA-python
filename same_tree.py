# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    # If both nodes are None, they are the same
    if not p and not q:
        return True
    # If one is None and the other is not=>they are different
    if not p or not q:
        return False
    # If values are different=>trees are different
    if p.val != q.val:
        return False
    # Recursively checking left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTree(p, q)) 

p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))

print(isSameTree(p, q))  
