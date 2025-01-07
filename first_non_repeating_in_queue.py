from collections import deque

def first_non_repeating(stream):
    char_count = {}  # Initializing Dictionary for  storing character frequencies
    queue = deque()  # Queue to maintain the order of characters.
    result = []      # List to store the result for each character in the input.

    for char in stream:
        # if the character is present in the dictionary already,, then increase the count +1.otherwise add the new one
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        # Add the character to the queue
        queue.append(char)

        # Checking the queue's front for the first non-repeating character
        while queue and char_count[queue[0]] > 1:
            queue.popleft()  # Remove the repeating character from the front#becos of deque we are using this.

        # Append the first non-repeating character to the result if queue is present
        if queue:
            result.append(queue[0])
        else:#just add #
            result.append('#')

    return ''.join(result)###for printing the final result in the form of string



stream = "aabc"
outputfinal = first_non_repeating(stream)
print(f"Input stream: {stream}")
print(f"First non-repeating characters: {outputfinal}")
