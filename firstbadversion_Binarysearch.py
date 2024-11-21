# First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
def isBadVersion(version):
    bad = 4
    return version >= bad


def firstBadVersion(n):
    left=1
    right=n

    while left < right:
        mid = (left+right)//2
        if isBadVersion(mid):  # Check if mid is a bad version or not..if yes follow the below condition.or follow the else
            right = mid  # Move right and keep it at mid
        else:
            left = mid + 1  # Move the left to mid+1
    #left will move beyond right...that is the position and loop will end there .
    return left  # left=> points to the first bad version



n = 5
print("First bad version:", firstBadVersion(n))
