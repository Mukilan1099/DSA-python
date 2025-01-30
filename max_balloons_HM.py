# Leetcode 1189: Maximum Number of Balloons using a hashmap

def maxNumberOfBalloons(text):
    char_count = {}
#counting how many letters and its recuurence in the given input..
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    # balloon contains what are the characters and its recurrenece
    required_chars = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1
    }

    min_instances = float('inf')  # Set tolarge value like a infinity..so that every value will be less than this ..for comparing..

    for char, required in required_chars.items():
        if char in char_count:
            min_instances = min(min_instances, char_count[char] // required)
        else:
            return 0  # If any required character is missing, return 0...

    return min_instances

print(maxNumberOfBalloons("nlaebolko"))        
# print(maxNumberOfBalloons("loonbalxballpoon"))  
# print(maxNumberOfBalloons("leetcode"))        
