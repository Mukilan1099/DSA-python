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
            # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        slow = dummy
        fast = dummy

        # Move fast `n + 1` steps ahead to create a gap of `n` nodes
        for i in range(n + 1):
            if fast is None:
                return None  # If n is larger than the length of the list, do nothing
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next


        slow.next = slow.next.next


        self.head = dummy.next

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
linked_list = LinkedList()
for value in [1, 2, 3, 4, 5]:
    linked_list.append(value)

print("Original list:")
linked_list.display()

# Remove the 2nd node from the end
linked_list.remove_from_end(2)

print("After removing 2nd node from end:")
linked_list.display()

