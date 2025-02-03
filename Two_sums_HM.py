# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSums(nums, target):
    num_map = {} 
    
    for i, num in enumerate(nums):
        complement = target - num  
        
        if complement in num_map:  # Checking if complement exists in dictionary which we initiallized.
            return [num_map[complement], i]  # => indices of complement and current number
        
        num_map[num] = i  

nums = [2, 7, 11, 15]
target = 9
print(twoSums(nums, target)) 
