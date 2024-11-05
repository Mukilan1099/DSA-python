#Problem 1: Find the Length of the Linked List
#Write a function to find the number of nodes in a linked list.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node
#
#     def get_length(self):
#         count = 0
#         current = self.head
#         while current is not None:
#             count += 1
#             current = current.next
#         return count
#
#
# linked_list = LinkedList()
# linked_list.append(3)
# linked_list.append(5)
# linked_list.append(8)
# linked_list.append(7)
#
# print("Length of linked list:", linked_list.get_length())



#Problem 2: Reverse the Linked List
#Write a function to reverse a linked list, so the last node becomes the head, and the head becomes the last node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(5)
linked_list.append(8)

print("Original list:")
linked_list.display()

linked_list.reverse()
print("Reversed list:")
linked_list.display()