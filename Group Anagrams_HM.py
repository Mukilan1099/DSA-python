# 49. Group Anagrams

# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)  

    for word in strs:
        sorted_key = tuple(sorted(word))  # Sorting characters in the word#ascending
        anagram_map[sorted_key].append(word)  # Group words with the same sorted key

    return list(anagram_map.values())  # Return grouped anagrams as a list of lists


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
