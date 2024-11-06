#Problem 3: Find the Middle Element of the Linked List

#Write a function to find the middle node in a linked list. If the list has an even number of nodes, return the first middle node.


#slow and fast pointer method =>easy to implement.fast moves with 2x and slow moves with 1x,when fast reaches the end,then the slow is at the middle=>which is half the distance
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
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def find_middle(self):
#         slow = self.head
#         fast = self.head
#
#         while fast is not None and fast.next is not None:
#             slow = slow.next        # Move slow pointer by 1x=>1 step forward moving
#             fast = fast.next.next    # Move fast pointer by 2x=>2 step forward moving
#
#         # When fast reaches the end, slow is at the middle
#         return slow.data if slow is not None else None
#
#
# linked_list = LinkedList()
# for value in [1, 2, 3, 4, 5]:
#     linked_list.append(value)
#
# print("Middle Element is:", linked_list.find_middle())
#

#problem:4
#Detect a Cycle in a Linked List
#Write a function to detect if there is a cycle in a linked list. A cycle occurs when a node's next pointer points back to a previous node, creating a loop. If there’s a cycle, return True; otherwise, return False.

#chatgpt=>generates this solution and i am understanding how this works.

class Node:
    def __init__(self, data):
        self.data = data  # Stores the data of the node
        self.next = None  # Points to the next node, initially None


class LinkedList:
    def __init__(self):
        self.head = None  # The head of the linked list, initially None

    # Method to append a node at the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
        else:
            # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to detect if the linked list has a cycle
    def has_cycle(self):
        slow = self.head  # Slow pointer starts at the head
        fast = self.head  # Fast pointer also starts at the head

        # Traverse the list with two pointers: slow moves 1 step, fast moves 2 steps
        while fast and fast.next:
            slow = slow.next  # Slow moves one step
            fast = fast.next.next  # Fast moves two steps

            # If slow and fast pointers meet, there's a cycle
            if slow == fast:
                return True  # Cycle detected

        # If fast pointer reaches the end of the list, there's no cycle
        return False

#####until this it is understood


# Create a new LinkedList instance
linked_list = LinkedList()

# Append nodes to the linked list
for value in [1, 2, 3, 4, 5]:
    linked_list.append(value)

# Create a cycle for testing (node 5 points back to node 3)
cycle_start = linked_list.head.next.next  # Node with value 3
current = linked_list.head
while current.next:
    current = current.next
current.next = cycle_start  # Create the cycle by pointing 5 to 3

# Detect if the linked list has a cycle
print("Cycle detected:", linked_list.has_cycle())  # Output should be True

# If you want to test with no cycle, uncomment the next line to break the cycle
current.next = None

# Detect again to see if cycle is removed
print("Cycle detected after removing cycle:", linked_list.has_cycle())  # Output should be False
