# class Node:
#     data=None
#     pointer=None####initially only the data should be there.the pointer denotes the address.It can be created when creating the second node.
#
#     def __init__(self,data):
#         self.data=data
#
# node1=Node(1)
# print(node1.data)
# print(node1.pointer)

###############################
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.pointer=None
#
# head=Node(1)#first node is called head
# node2=Node(2)
# node3=Node(3)
#normally when we we want to link the nodes.1st node pointer is the second node address and so on.
##instead of keeping the node2.value and node2.pointer ,we need the node2 address.so just keep the node2

# head.pointer=node2###as we are getting the address only when we printed node2 we can easily map this head pointer is equal to node2
# node2.pointer=node3
#
# print(head)
# print(head.pointer)
# print(node2)
# print(node2.pointer)
# print(node3)

# print(head.data)
# print(head.pointer)
# print(head)###prints the address of the head.----hexadecimal
# print(id(head))###prints the address in the  decimal
# print(node2)###here we can see when printed,the head.pointer and also the node2 is in the same memory.


#we are checking whether the values are present in the linked list or not.

# cur = head###it should be stored in one variable as the head is more important.
# while cur is not None:
#     print(cur.data)
#     cur=cur.pointer
# print(head.data)
# # print(cur.data)##it will give error.
# print(cur)##shows none.as the last node has no value:only None.




#------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def add(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer=newNode

    def print(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.pointer




linkedlist=Linkedlist()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist.print()

