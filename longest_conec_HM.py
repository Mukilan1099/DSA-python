# Longest Consecutive Sequence
# (LeetCode Problem #128)

# Description:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


def longest_consecutive(nums):
    num_set = set(nums)##avoid duplicates and reduce the time of operation
    longest_streak = 0

    for num in num_set:
        # Only start counting if it is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak


nums = [100, 4, 200, 1, 3, 2]


print(longest_consecutive(nums))  
