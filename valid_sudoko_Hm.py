# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


from collections import defaultdict
def isValidSudoku(board):
    
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)  

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num == '.':  # Skipping  tha empty ones
                continue

            # if no.is alreasy present,then it is false.
            if num in rows[i] or num in cols[j] or num in boxes[(i // 3, j // 3)]:
                return False

            # Adding number to row, column, and 3x3 box
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i // 3, j // 3)].add(num)

    return True

sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(isValidSudoku(sudoku_board))
