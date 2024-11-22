# Given a positive integer num, return true if num is a perfect square or false otherwise.
#
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
#
# You must not use any built-in library function, such as sqrt.


#using binary search we are solving this as it will take less time complexity.
def isPerfectSquare(num):#2 pointer technique
    if num < 1:
        return False  # first this logic=>No perfect square exists for numbers less than 1

    low=1#initialise at first
    high=num#initialise at number which gave

    while low <= high:
        mid = (low + high) // 2

        square = mid * mid  # take square of value

        if square == num:
            return True  # perfect square=>is found.so true.
        elif square < num:
            low = mid + 1  #move pointer left to mid+1
        else:
            high = mid - 1  #move pointer high to mid -1

    return False  # No perfect square found=>loop exits .when low>high

print(isPerfectSquare(25))