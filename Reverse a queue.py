#Reverse a Queue.

#Simple Problem.

#using deque
# from collections import deque
#
# def reverse_queue(q):
#     stack = []
#     while q:##until q becomes empty.##take from q and append to stack in required order.
#         stack.append(q.popleft())
#     while stack:#until stack becomes empty  ##again take from stack and append to q.
#         q.append(stack.pop())
#     return q
#
#
# queue = deque([1, 2, 3, 4, 5])
# print("Original Queue:", queue)
# print("Reversed Queue:", reverse_queue(queue))

##Using normal list
def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.pop(0))  # Remove from the front of the list..using pop.

    while stack:
        q.append(stack.pop())  # Add to the end of the list.

    return q


queue = [1, 2, 3, 4, 5]
print("Original Queue:", queue)
print("Reversed Queue:", reverse_queue(queue))

