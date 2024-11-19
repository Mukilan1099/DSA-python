###two types of searching.
# 1.Linear search-o(n)
# 2.Binary search -o(logn)
#
# 1.Linear search:
# search through the list or array for checking the element present in it or not.If present,return the index of it.
#     worst case:0(n).
# 2.Binary search:Implemenst when the elements are sorted in ascending order only.
# Implements two pointer technique:oone at first ,another at last.
# using first and last,calculate the center element using //=>only takes quotient.
# As we can found the middle element.we can check the middle element with the given input number to find.=>we need to check whether it is smaller or larger.
# based on this we are moving the pointers...ignoring the one side ..
# and again implement the same logic...until we get this.

# Linear search:
# a=[1,2,3,4,5]
# input=5
# for i in range(0,len(a)):
#     if a[i]==input:
#         print(i)
#         break
# else:
#     print("no it is not present")

#Binary search

def binary_search(nums, target):
    #initializing two pointers
    left=0#first index
    right=len(nums)-1#last index

    while left <= right:###loop should continue until left <=right
        mid = (left+right)//2  # Calculate the mid-point.center element..only takes quotient

        if nums[mid] == target:  # Check if the target is at the mid-point or not.if present return the index=>which is mid.
            return mid
        elif nums[mid] < target:  # If target is greater, ignore the left half.move the left pointer to right.one step after mid
            left = mid + 1
        else:  # If target is smaller, ignore the right half.move the pointers..move the right pointer to left.one step before left
            right = mid - 1

    return -1  # If target is not present,then return only the -1.


nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = binary_search(nums, target)
print("Index of target is:", result)

