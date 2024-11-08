#problem:
#Move last element to front of a given Linked List
#description for solving this:
#To move the last element of a linked list to the front, you need to perform the following steps:

#1.Traverse to the end of the list to find the last node and the second-last node.
#2.Set the next pointer of the second-last node to None to remove the link to the last node.
#3.Make the last node point to the current head of the linked list.
#4.Update the head of the list to be the last node.

# Define Node and LinkedList classes with move_last_to_front and display methods
##we are going to use the two pointer techniques for solving this.
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
            while current.next:
                current = current.next
            current.next = new_node

    def move_last_to_front(self):
        dummy = Node(0)##we initializing a dummy node first.
        dummy.next = self.head

        if not self.head or not self.head.next:
            return

        second_last = dummy#keep this pointer in the dummy node.(before 1st)
        last = self.head#keep this in the first node.


        while last.next:
            second_last = last
            last = last.next
            # traverse until last reaches the last node
            # second_last will each the postion 2nd last .

        second_last.next = None#make this as none so it get disconnected from the last node
        last.next = dummy.next#assign the last to first.
        self.head = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# Create a linked list with elements 1, 2, 3, 4, 5
linked_list = LinkedList()
for i in range(1, 6):
    linked_list.append(i)

print("Original List:")
linked_list.display()

# Move the last node to the front
linked_list.move_last_to_front()
print("\nAfter moving the last element to front:")
linked_list.display()

