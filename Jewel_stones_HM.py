# 771. Jewels and Stones
#
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones(jewels, stones):
    #initializing a dictionary-Here count each ..how many are stones are there.
    stone_count = {}
    for stone in stones:
        if stone in stone_count:
            stone_count[stone] += 1  # If stone  already exists=> +1
        else:
            stone_count[stone] = 1  # If stone is new, add it with count 1

    # Counting how many stones are jewels.Iterating the jewels and seeing how many it is present in the stone_count
    jewel_count = 0
    for jewel in jewels:
        if jewel in stone_count:  # Check if the jewel exists in the HashMap(which means the jewel is found in stone_count.)
            jewel_count += stone_count[jewel]

    # Return => total number of jewels
    return jewel_count

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
