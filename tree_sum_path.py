# Problem: 437. Path Sum III
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of values along the path equals targetSum.

# A path does not need to start at the root or end at a leaf, but it must go downward (from parent to child).
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

    def countPathsFromNode(self, node, targetSum):
        if not node:
            return 0

        count = 0
        if node.data == targetSum:
            count += 1

        count += self.countPathsFromNode(node.left, targetSum - node.data)
        count += self.countPathsFromNode(node.right, targetSum - node.data)

        return count

    def pathSumHelper(self, node, targetSum):
        if not node:
            return 0

        return (self.countPathsFromNode(node, targetSum) + 
                self.pathSumHelper(node.left, targetSum) + 
                self.pathSumHelper(node.right, targetSum))

    def pathSum(self, targetSum):
        return self.pathSumHelper(self.root, targetSum)

    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left:
            self.display(node.left, level + 1, "L--> ")
        if node.right:
            self.display(node.right, level + 1, "R--> ")




tree1 = Tree()
tree1.add(10)
tree1.add(5, 10, True)
tree1.add(-3, 10, False)
tree1.add(3, 5, True)
tree1.add(2, 5, False)
tree1.add(11, -3, False)
tree1.add(3, 3, True)
tree1.add(-2, 3, False)
tree1.add(1, 2, False)

tree1.display()
print("Number of paths with sum 8:", tree1.pathSum(8)) 


tree2 = Tree()
tree2.add(1)
tree2.add(2, 1, True)
tree2.add(3, 1, False)

tree2.display()
print("Number of paths with sum 5:", tree2.pathSum(5)) 
