# Problem: 236. Lowest Common Ancestor of a Binary Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentData=None, isLeft=True):
        node = TreeNode(data)

        if not self.root:
            self.root = node
            return

        parentNode = self.findNode(parentData, self.root)
        if not parentNode:
            print("Parent node not found")
            return
        
        if isLeft:
            if parentNode.left is None:
                parentNode.left = node
            else:
                print(f"Parent {parentData} already has a left child.")
        else:
            if parentNode.right is None:
                parentNode.right = node
            else:
                print(f"Parent {parentData} already has a right child.")

    def findNode(self, data, node):
        if node is None:
            return None
        if node.data == data:
            return node
        leftSearch = self.findNode(data, node.left)
        return leftSearch if leftSearch else self.findNode(data, node.right)

    def lowestCommonAncestor(self, node, p, q):
        if not node or node.data == p or node.data == q:
            return node

        left = self.lowestCommonAncestor(node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)

        if left and right:
            return node  

        return left if left else right

    def findLCA(self, p, q):
        return self.lowestCommonAncestor(self.root, p, q)

    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left:
            self.display(node.left, level + 1, "L--> ")
        if node.right:
            self.display(node.right, level + 1, "R--> ")

tree1 = Tree()
tree1.add(3)
tree1.add(5, 3, True)
tree1.add(1, 3, False)
tree1.add(6, 5, True)
tree1.add(2, 5, False)
tree1.add(0, 1, True)
tree1.add(8, 1, False)
tree1.add(7, 2, True)
tree1.add(4, 2, False)

tree1.display()
lca_node = tree1.findLCA(5, 1)
print("Lowest Common Ancestor of 5 and 1:", lca_node.data)  

lca_node = tree1.findLCA(6, 4)
print("Lowest Common Ancestor of 6 and 4:", lca_node.data)  
