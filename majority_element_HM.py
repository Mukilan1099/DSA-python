# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


from collections import defaultdict

def majorityElement(nums):
    count_map = defaultdict(int)  
    majority_count = len(nums) // 2  # Majority threshold :if anything is greater than this, it is majority

    for num in nums:
        count_map[num] += 1  # we are increasing count
        if count_map[num] > majority_count:  # Checking whether it is a majority or not
            return num  #if it is true return it

    return -1  # we are assuming the array contains majority element.If it not presetn then it will return -1..Eg.[1,2,3,4,5]

# nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
# nums3=[1,2,3,4,5]
# print(majorityElement(nums1))  
print(majorityElement(nums2)) 
# print(majorityElement(nums3))  
