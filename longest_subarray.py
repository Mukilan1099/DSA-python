# Problem: Longest Subarray with Sum Equals K
# Leetcode Problem: Given an integer array nums and an integer k, return the length of the longest subarray whose sum equals k.


def maxSubArrayLen(nums, k):
    prefix_sum = 0  # Running cumulative sum
    max_length = 0  # Longest subarray length
    prefix_map = {}  # Stores prefix_sum and its first occurrence index

    for i, num in enumerate(nums):
        prefix_sum += num  #cumulative sum

        # Check if the entire subarray from the start to i sums to k.
        if prefix_sum == k:
            max_length = i + 1

        # Checking if (prefix_sum - k) exists in the hashmap or not...
        if (prefix_sum - k) in prefix_map:
            # Update max_length to the larger value
            max_length = max(max_length, i - prefix_map[prefix_sum - k])###used chatgpt and understood this line

        # Store the prefix_sum in the map if it is not present...
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length
nums = [1, -1, 5, -2, 3]
k = 3
print(maxSubArrayLen(nums,k))