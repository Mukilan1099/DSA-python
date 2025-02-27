# 543. Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.max_diameter = 0  # To store the maximum diameter found

    def add(self, data, parentData=None):
        node = TreeNode(data)

        if not self.root:
            self.root = node
            return

        parentNode = self.findNode(parentData, self.root)
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

    def diameter(self, node):
        if not node:
            return 0

        # Store =>heights of all children
        heights = sorted([self.diameter(child) for child in node.children], reverse=True)

        # Take top two heights (if available)
        max_height = heights[0] if heights else 0
        second_max_height = heights[1] if len(heights) > 1 else 0

        # Updating => max_diameter
        self.max_diameter = max(self.max_diameter, max_height + second_max_height)

        return 1 + max_height  #height of this subtree

    def getDiameter(self):
        self.max_diameter = 0  # Reseting=> before calculation
        self.diameter(self.root)
        return self.max_diameter

    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)



tree = Tree()
tree.add(1)
tree.add(2, 1)
tree.add(3, 1)
tree.add(4, 1)
tree.add(5, 2)
tree.add(6, 2)
tree.add(7, 3)
tree.add(8, 3)
tree.add(9, 4)
tree.add(10, 5)
tree.add(11, 10)

tree.display()
print("Diameter of Tree:", tree.getDiameter())  
