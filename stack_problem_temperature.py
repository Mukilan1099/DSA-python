# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

##this code i got from chatgpt and came to know how it is working and understood.

def dailyTemperatures(temperatures):
    #initialising the empty list with no.of 0s as the temperatures input.
    n = len(temperatures)
    answer = [0] * n
    stack = []  # This will store indices

    #  Process each day
    for i in range(n):
        # While stack is not empty and the current temperature is warmer than the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()  # Get the previous day's index
            answer[prev_index] = i - prev_index  # Calculate the number of days
        # Push the current day's index onto the stack
        stack.append(i)

    return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))