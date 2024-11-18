##algo problem:

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.




class MinStack:

    def __init__(self):###initialising two stacks..
        self.stack = []  # Regular stack to store all elements
        self.min_stack = []  # Stack to store the minimum values

    def push(self, val: int) -> None:##add value to stack and also min_stack..but for min_stack-condition need to get applied.
        self.stack.append(val)
        # Add the new minimum to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            # Remove from min_stack if it matches the popped value
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

# inputs:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
