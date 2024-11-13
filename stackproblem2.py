# problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s):
    # Dictionary for matching closing to opening brackets==Initializing
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    # Loop over each character in the string
    for char in s:
        if char in bracket_map:
            # If it's a closing bracket, pop from the stack if it's not empty
            top_element = stack.pop() if stack else '#'#we are keeping it in the separate variable.

            # Check if this closing bracket matches the last opened bracket
            if bracket_map[char] != top_element:#now we are accesing the character match in the dictionary which we created.and seeing.if it matches or not.
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)###if it is opening bracket we are adding it to the empty stack which we created.

    # If stack is empty, all brackets matched; otherwise, some were unmatched
    return not stack#everything is matched ,then it is removed ,it becomes empty.


s = "({[]})"
result=isValid(s)
print(result)