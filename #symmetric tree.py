#symmwetric tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # In this we assuming a binary tree

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
        
        #  binary tree (at most 2 children)=>confirming
        if len(parentNode.children) < 2:
            parentNode.children.append(node)
        else:
            print(f"Node {parentData} already has 2 children. Cannot add {data}.")

    def findNode(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            nodeFound = self.findNode(data, child)
            if nodeFound:
                return nodeFound
        return None

    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True  # Both are None → Symmetric
        if not node1 or not node2:
            return False  # One is None, the other isn't → Not symmetric
        if node1.data != node2.data:
            return False  #no match → Not symmetric

        # Checking thew  left subtree is a mirror of the right subtree
        if len(node1.children) == 2 and len(node2.children) == 2:
            return self.isMirror(node1.children[0], node2.children[1]) and self.isMirror(node1.children[1], node2.children[0])
        elif len(node1.children) == 1 and len(node2.children) == 1:
            return self.isMirror(node1.children[0], node2.children[0])
        elif len(node1.children) == 0 and len(node2.children) == 0:
            return True
        return False  # diff no.of  children

    def isSymmetric(self):
        if not self.root:
            return True
        return self.isMirror(self.root, self.root)

    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)



print("Test Case 1: Symmetric Tree")
tree1 = Tree()
tree1.add(1)
tree1.add(2, 1)
tree1.add(2, 1)
tree1.add(3, 2)
tree1.add(4, 2)
tree1.add(4, 2)
tree1.add(3, 2)

tree1.display()
print(tree1.isSymmetric()) 

print("\nTest Case 2: Asymmetric Tree")
tree2 = Tree()
tree2.add(1)
tree2.add(2, 1)
tree2.add(2, 1)
tree2.add(3, 2)
tree2.add(3, 2)

tree2.display()
print(tree2.isSymmetric()) 
