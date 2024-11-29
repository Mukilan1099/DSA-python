# Search in Rotated Sorted Array
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    low=0
    high=len(nums)-1

    while low <= high:
        mid = (low + high) // 2

        # Check if the mid element is the target=>finding middle element
        if nums[mid] == target:
            return mid

        # Determine which half is sorted=>based on which side is the sorted array,we are moving te pointers.
        if nums[low] <= nums[mid]:#searcing in left alf
            # Left half is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1  # Target is in the left half
            else:
                low = mid + 1  # Target is in the right half
        else:#searcing in right half
            # Right half is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1  # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half

    return -1  # Target is not found

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))
