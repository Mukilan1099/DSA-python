#(LeetCode Problem: 209. Minimum Size Subarray Sum)
##Given an array of positive integers nums and a positive integer target, find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If no such subarray exists, return 0.


def min_subarray_len(target, nums):
    ###initilasing the two pointers
    left = 0  # Initialize the left pointer
    right = 0  # Initialize the right pointer
    minimum = []  # List to store the lengths of valid subarrays.from this in final we are taking the mininum and returning
    subSum = 0  # Variable to store the current subsum of the window

    while right < len(nums):  # moving  until right pointer reaches the last element of array
        subSum += nums[right]  # Add the current element to the window's sum..eg:if 2,3,5 is there adding :10 will be in th subsum

        # Shrink the window from the left while the sum is >= target
        while subSum >= target:###if the subsum reaches the target or equal and then we should shrink the window by moving the left pointer to right.
            minimum.append(right - left + 1)  # Append the window's length to the list##as this is the index we need to add 1.left0,right 3=>3-0+1=4..length b/w left and right.
            subSum -= nums[left]  # Remove the leftmost element from the sum..##shrinking the left by moving +1 from left ,,also which means reduce the subsum from the old left element which included.
            left += 1  # Move the left pointer forward

        right += 1  # Move the right pointer forward# when the above while ends or fails

    # Return 0 if no valid subarray exists otherwise return the smallest subarray length by the else=>min(minimum)
    return 0 if len(minimum) == 0 else min(minimum)

print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))

