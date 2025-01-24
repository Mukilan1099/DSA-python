# Longest Substring Without Repeating Characters

# Sliding Window + HashMap

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}  # HashMap=> to store the last seen index of characters
    max_length = 0  #to track the maximum length
    start = 0  # Left pointer of the sliding window...keeep it at start.

    for end in range(len(s)):  # Right pointer traverses the string....
        char = s[end]

        if char in char_map and char_map[char] >= start:
            # Move start to the right of the last seen index
            start = char_map[char] + 1

        # keep. the character latest index in the map
        char_map[char] = end

        # length of the current substring
        max_length = max(max_length, end - start + 1)

    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
