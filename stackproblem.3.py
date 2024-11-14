#Algo problems:3-Medium

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


def RPN(tokens):
    # Initialize=>stack
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:#if the token contains the operators=>need to pop the last two number from the stack and insert this operation..for minus and divide it should be in order.
            # Pop the last two numbers for the operation
            b = stack.pop()
            a = stack.pop()

            # Apply the operation
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                # For division, use int() to truncate towards zero
                result = int(a / b)###here example:7/2=3.5...when we do int(3.5)means it will give 3..so we are using this logic

            # Push the result back onto the stack
            stack.append(result)
        else:
            # Convert the token to an integer and push onto stack
            stack.append(int(token))###if the token contains the number we need to add into the stack.

    # The final result is the only element left in the stack
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(RPN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print(RPN(tokens))
