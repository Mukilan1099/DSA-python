# Algo problem:
# Baseball game:
#
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
#
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
#
def calPoints(operations):
    stack = []  # Initializing an empty stack to keep track of the scores.

    for op in operations:
        if op == '+':#### Sum of the only the last two scores
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':#### Double the last score
            stack.append(2 * stack[-1])
        elif op == 'C':# Remove the last one..as pop removes the last one it is used
            stack.pop()
        else:
            # Add a new score###if any integer is there,we need to append this integer to the stack.
            stack.append(int(op))

    # Sum or total of  up all the values in the stack
    return sum(stack)
# operations = ["5","2","C","D","+"]
# print(calPoints(operations))
operations = ["5","-2","4","C","D","9","+","+"]
print(calPoints(operations))
# operations = ["1","C"]
# print(calPoints(operations))

