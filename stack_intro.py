# #stack: Introduction to the stack data structure in the DSA.
# LIFO-Last in first out
# FILO-first in last out
#
# used in the back and forward in the web browser=>
# eg.when we are taking out the 3 values from the stack which consists of 5 values=>the taken values are kept in another stack
# eg:undo and redo
#
#
# Operations:
# 1.Accessing: not like array,array can be accesed by the index value-o(1).here it is not able to access via indexing..have to take out everything-o(n)
# 2.Insertion:applicable only if we want to acces the last one....insertion.as we want to add to a new position other than this we need to take everything out and need to insert.so not applicable..only applicable for the last in first out.
# 3.Deletion:same as before...
# choose the stack only if there is a need for change in the last one in these 3 operations.not
# 4.Searching:if it is a last one it can be used.
#
# Names used in the stack:
# 1.Accessing
# 2.Insertion or  PUSH
# 3.Deletion or POP
# POP=>removes the last element and will show.
# Top=>it will show the last element added to the stack.
#
# stack initializing in two ways:
# 1.Dequeue
# 2.List used as a stack.

# 2.
# stack=[]
# #accessing
# stack=[1,2,3,4]
# print(stack[-1])
#
# #2 concepts:
# stack=[]
# stack underflow=>stack[-1]#when nothing is there ,we are trying to access.
# stack overflow=>#when there is only 2 elements and we are trying to access the extra one.
#
#
# #Insertion.
# stack=[1,2,3,4]
# stack.append(5)
# print(stack)
#
# #deletion
# stack.pop()
# #deletes the last one.
#
# in these cases only we can use efficiently the stack for only the operation involving the last ones.
#
#     #searching
# stack = [1, 2, 3, 4]
# X=4
# if stack[-1]==X:
#     print("true")



#stack implementing using dequeue
#collection module is needed for this

from collections import deque
stack=deque([1,2,3,4])
print(stack)
print(type(stack))


print(stack[-1])#access
stack.append(5)#insertion
print(stack)

stack.appendleft(5)###special in the deque
print(stack)
stack.popleft()#special
stack.pop()
print(stack)


