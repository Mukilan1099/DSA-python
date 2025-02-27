# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

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

    def isBalancedHelper(self, node):
        if not node:
            return 0, True  

        # Storing the heights of all children
        heights = []
        balanced = True

        for child in node.children:
            height, isBal = self.isBalancedHelper(child)
            heights.append(height)
            if not isBal:
                balanced = False

        # Finding=>max and min height
        max_height = max(heights) if heights else 0
        min_height = min(heights) if heights else 0

        # Checking balance condition
        if max_height - min_height > 1:
            balanced = False

        return 1 + max_height, balanced

    def isBalanced(self):
        _, balanced = self.isBalancedHelper(self.root)
        return balanced

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
print(tree.isBalanced()) 


balancedTree = Tree()
balancedTree.add(1)
balancedTree.add(2, 1)
balancedTree.add(3, 1)
balancedTree.add(4, 2)
balancedTree.add(5, 2)
balancedTree.add(6, 3)
balancedTree.add(7, 3)

balancedTree.display()
print(balancedTree.isBalanced())  
