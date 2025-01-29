# 242. Valid Anagram

# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.
def isAnagram(s, t):
    # Lengthnot same=>not an anagram
    if len(s) != len(t):
        return False

    # hashmap=> (dictionary)=> to count character frequencies
    char_count = {}

    # first=>Count characters in string s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract character counts using string t......subtractin the count in the char_count.
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:##conditions for false
            return False

    # If all counts are zero, strings are anagrams
    return all(count == 0 for count in char_count.values())
##all() is a Python built-in function that returns True if all elements in the given iterable (in this case, the generator expression) evaluate to True.
# If at least one count is not 0, all() will return False.


s1 = "anagram"
t1 = "nagaram"
print(isAnagram(s1, t1))  

# s2 = "rat"
# t2 = "car"
# print(isAnagram(s2, t2)) 
