# Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.

def findMin(nums):#2 pointeres initiation
    low=0
    high=len(nums)-1

    while low < high:
        mid = (low + high) // 2

        # If the middle element is greater than the last element,
        # then the minimum is in the right half
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            # The minimum is in the left half (including mid)
            high = mid#move the pointer high to mid

    # When low == high, we've found the minimum
    return nums[low]

nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # Output: 0
