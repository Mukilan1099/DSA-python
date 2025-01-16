# Problem: Subarray Sum Equals K (LeetCode 560)
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

def subarraySum(nums, k):
    prefix_sum = 0  # This will store the cumulative sum as we iterate
    count = 0  # This will count the number of subarrays with sum equal to k....k is the input
    prefix_map = {0: 1}  # Initialize with {0: 1} to account for subarrays from the start(starting numbere itself equal to k so we are initializing)

    for num in nums:
        prefix_sum += num

        # Checking if (prefix_sum - k) exists in the prefix_map,if it exists we are adding the count.
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]

        # Update the prefix_map with the current prefix_sum
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] += 1
        else:
            prefix_map[prefix_sum] = 1

    return count

nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7

print(subarraySum(nums, k))
