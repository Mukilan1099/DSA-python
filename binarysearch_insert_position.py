# Search Insert Position:
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

def search_insert(nums, target):#2 pointer techniques.
    left = 0  # first index
    right = len(nums) - 1  # last index

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:  # If target >mid, search the right half
            left = mid + 1
        else:  # If target <mid>, search the left half
            right = mid - 1

    # If not found=> left will point to the correct insert position
    return left

nums = [1, 3, 5, 6]
# target = 5
# print("Insert position:", search_insert(nums, target))

target = 2
print("Insert position:", search_insert(nums, target))

# target = 7
# print("Insert position:", search_insert(nums, target))

# target = 0
# print("Insert position:", search_insert(nums, target))
