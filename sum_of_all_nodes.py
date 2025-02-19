# Problem: Find the Sum of All Nodes in a Tree
# Problem Statement:
# Given the root of a tree, return the sum of all node values

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

    def sumNodes(self, node=None):
        if not node:
            node = self.root
        return node.data + sum(self.sumNodes(child) for child in node.children)

tree = Tree()
tree.add(1)
tree.add(2, 1)
tree.add(3, 1)
tree.add(4, 2)
tree.add(5, 2)
tree.add(6, 3)
tree.add(7, 3)

print(tree.sumNodes())

#if we need to display we can add a display function
