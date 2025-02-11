# #Tree data structure
# ##Introduction

# #it is a non-linear data structure
# it is like a organization chart or a family tree
# eg:employess in a company with hierarchial Order
#     -CEO
#         -VP
#             -Manager
#                 -Team Lead
#                     -Software Engineer
#                         -Intern


# it can be created through node only like linked list
# it is a collection of nodes
#     Diff b/w linked list and tree is in linked list we can have only one node but in tree we can have multiple nodes

# starting node is called root node

# other nodes are child nodes..
# 1
# 2
# 345
#     2 is parent of 3,4,5
#     3,4,5 are child of 2
#     1 is parent of 2
#     2 is child of 1

#     1 is parent of 2,3,4,5
#     2,3,4,5 are child of 1

# the node which does not have childnodes is called leaf nodes.
# Ancestor: the parent nodes of a node are called ancestor
# Descendant: the child nodes of a node are called descendant
# eg: 1 is ancestor of 2,3,4,5
#     2,3,4,5 are descendant of 1

#     2 is ancestor of 3,4,5
#     3,4,5 are descendant of 2

#     1 is ancestor of 3,4,5
#     3,4,5 are descendant of 1

#     1 is ancestor of 4,5
#     4,5 are descendant of 1

#     1 is ancestor of 5
#     5 is descendant of 1

#     2 is ancestor of 3,4,5
#     3,4,5 are descendant of 2

#     2 is ancestor of 4,5
#     4,5 are descendant of 2

#     2 is ancestor of 5
#     5 is descendant of 2

#     3 is ancestor of 4,5
#     4,5 are descendant of 3

#     3 is ancestor of 5
#     5 is descendant of 3

#     4 is ancestor of 5
#     5 is descendant of 4

#     1 is ancestor of 2
#     2 is descendant of 1

#     1 is ancestor of 3
#     3 is descendant of 1

#     1 is ancestor of 4
#     4 is descendant of 1

#     1 is ancestor of 5
#     5 is descendant of 1

#     2 is ancestor of 3
#     3 is descendant of 2

#     2 is ancestor of 4
#     4 is descendant of 2

#     2 is ancestor of 5
#     5 is descendant of 2

#     3 is ancestor of 4
#     4 is descendant of 3

#     3 is ancestor of 5
#     5 is descendant of 3

#     4 is ancestor of 5
#     5 is descendant of 4

#     1 is ancestor of 2,3
#     2,3 are descendant of 1

#     1 is ancestor of 2,4
#     2,4 are descendant of 1

#     1 is ancestor of 2,5
#     2,5 are descendant of 1

#     1 is ancestor of 3,4
#     3,4 are descendant of 1

# TRee max height: 
# the node which has the max no.of edges from the root...

# Depth:
# for specific node it is used.
#     from a particular node to the root node is called depth


# all operations can be done in tree.

# Eg: File Manager in mobile phone.=>hierarchial.



# --------------
class TreeNode:
  def __init__(self, data):###data used for creating the node
    self.data = data
    self.children=[]###instead of pointer in linked list we use children in tree becos many values are linked.

# treenode=TreeNode("Drinks")
# print(treenode.data)
# print(treenode.children)

class Tree:
  #starting is root.
  def __init__(self):
    self.root=None###node(root) is single value...but the child only many

  # def add(self,data):
  #   node=TreeNode(data) 

  #   if self.root is None:###if empty then add in root
  #     self.root=node#setting node in root

  def add(self,data,parentdata=None):#parentdata is used becos we need to know for which parent we are going to add this.
    node=TreeNode(data) 

    if self.root is None:###if empty then add in root
      self.root=node#setting node in root
      return#it is used instead of else. if the condition is true then it will return the value and come out of the function.
    

tree=Tree()
tree.add("3")
tree.add("5","3")#in parentdata we are giving 3 so 5 is child of 3

#continuity will be there.
# we need to find first where the node is present and then we need to add the child to that node.





