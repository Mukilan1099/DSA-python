# Queue:
# stack is opposite to array.(insertion and deletion)
# queue is ooposite to stack.
# queue=FIFO-First in Fitst Out.------LILO-last in last out
#
# First main opertations:
# Insertion
# deletion
# Accessing
# Search
#
# Deletion and Accessing can be done at one end only(stack and queue)
# Also we wont search using the stack and queue..
# we can search by only removing the elements.
# so for searching,we dont use the stack and queue(cant able to access like array.)
#
# Operations in queue:
# 1.Insertion
# 2.Deletion
# 3.Front
# 4.Isempty
#
# 1.Insertion:
# inserting one by one. Time Complexity 0(1)
# 2.Deletion:
# First inserted is deleted first.(opp to stack.)
# [1,2,3,4]
# if 1 is deleted ,then others will move one step left and last position becomes empty.not
#
# 3.Delete will remove the first element
# Front:we can acesss the first without deleting it.similar to the pop and top used in the
# the stack:
#
# 4.isempty:
# check,whether the queue is empty or not?
#
# Naming used in the queue:(insertion and deletion process )
# 1.Enqueue---push(stack)--Insertion
# 2.Dequeue---pop(stack)--Deletion
#
# Time complexity-0(n)--for all 4 operations.
# Space complexity-based on lenght. o(n)--eg:4 elements present 0(4)
#
# Types:
# 1.Simple Queue:
# First in First out
# Insert at back and access at front.
# Eg:Atm queue
#
# 2.Double ended queue:
# Simple queue+stack
# Eg:back and forward in web browser--Used in stack.next one is kept in separate stack.instead of that we can use the double ended queue.
#
# 3.Circular queue:
# circular motion.last is connected to first.
# eg.traffic signal . in 4 roads each road will have signals in a routine circiular.
#
# 4.Priority Queue:
# Eg.when standing in queue in hospital,if any emergency occurs this is treated first as priority.
#     when inserting 1,2 and then three,3 is inserted then and is accessed first.

# Implementation:
#
# queue can be initialised in many ways:
# 1. in List:
#4 operations used by list
# queue=[]
#
# #enqueue=>Addition
# queue.append(5)
# queue.append(6)
# queue.append('Messi')
#
# #Dequeue=>Deletion
# a=queue.pop(0)
# b=queue.pop(0)
# print(a,b)
#
# # Front=>used for access the first element
# print(queue[0])
#
# #isempty
# print(len(queue)==0)

####from Queue Data Structure

from queue import Queue
# q=Queue()###create object
q=Queue(maxsize=3)###optional
##enqueue
q.put("Monty")
q.put("cloud")
q.put("filling")

# for chekcing queue is full or not:
print(q.full())

##Dequeue
a=q.get()
# b=q.get()
print(a)

##front=>accessing 1st element
print(q.queue[0])
print(q.get())

print(q.empty())

###we can initialise the maxsize for queue in starting

#another method.
from collections import deque
#used for double ended queue
# we can insert at delete at both places as we learnt from the stack
##3methods used..popleft,popright etc..