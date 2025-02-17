class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentdata=None):
        node = TreeNode(data)
        
        if not self.root:  # If tree is empty=> set root
            self.root = node
            return
        
        parentNode = self.findNode(parentdata, self.root)
        
        if not parentNode:
            print("Parent Node not found")
            return
        
        parentNode.children.append(node)  # Add new node => child

    def findNode(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            foundNode = self.findNode(data, child)
            if foundNode:
                return foundNode
        return None

    def maxDepth(self, node=None):
        if node is None:
            node = self.root  
        
        if not node:  # tree => empty
            return 0
        
        if not node.children:  # If no children, it's a leaf node#meaning the depth of a single node is 1.
            return 1
        
        return 1 + max(self.maxDepth(child) for child in node.children)  # Recur for all children##calculating the maximum depth of the tree

    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)

tree = Tree()
tree.add(1)       # Root 
tree.add(2, 1)    # 2 is child of 1
tree.add(3, 1)    # 3 is child of 1
tree.add(4, 2)    # 4 is child of 2
tree.add(5, 2)    # 5 is child of 2
tree.add(6, 3)    # 6 is child of 3
tree.add(7, 3)    # 7 is child of 3
tree.add(8, 4)    # 8 is child of 4

tree.display()  


print("Maximum Depth of Tree:", tree.maxDepth())  
