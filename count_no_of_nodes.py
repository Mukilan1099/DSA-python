# Count the Number of Nodes in a Tree
# Problem Statement:
# Given the root of a tree, return the total number of nodes in the tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentdata=None):
        node = TreeNode(data)
        if not self.root:
            self.root = node
            return
        parentNode = self.findNode(parentdata, self.root)
        if not parentNode:
            print("Parent node not found")
            return
        parentNode.children.append(node)

    def findNode(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            nodeFound = self.findNode(data, child)
            if nodeFound:
                return nodeFound
        return None

    def countNodes(self, node=None):
        if not node:
            node = self.root
        return 1 + sum(self.countNodes(child) for child in node.children)


tree = Tree()
tree.add(1)
tree.add(2, 1)
tree.add(3, 1)
tree.add(4, 2)
tree.add(5, 2)
tree.add(6, 3)
tree.add(7, 3)

print(tree.countNodes())  
