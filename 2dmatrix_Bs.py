#search a 2D matrix
# You are given an m x n integer matrix matrix with the following two properties:
#
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix, target):
    # Get dimensions of the matrix
    m = len(matrix)  # number of rows
    n = len(matrix[0])  # number of columns

   #initialising
    low = 0
    high = m * n - 1  # Treat the matrix as a 1D array=>which means [[1, 3, 5], [7, 9, 11], [13, 15, 17]]

    while low <= high:
        mid = (low + high) // 2

        # Convert mid to row and column
        row = mid // n #quotient row
        col = mid % n #reminder=>column

        # Get the element at the current mid position#As it is a matrix format,row and column.
        mid_value = matrix[row][col]

        # Compare with the target
        if mid_value == target:
            return True  # Target found
        elif mid_value < target:
            low = mid + 1  # Move to the right half +1from mid
        else:
            high = mid - 1  # Move to the left half -1 from mid

    return False  # Target not found


matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target = 9

print(searchMatrix(matrix, target))
