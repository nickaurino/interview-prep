from harness import run

# Valid Sudoku (LeetCode #36) — hash sets per row / column / 3x3 box.
# One pass over the board; box index computed from (r//3, c//3). O(81) = O(1) for a fixed 9x9 board.


def is_valid_sudoku(board):
    rows_sum = [set() for _ in range(9)]
    cols_sum = [set() for _ in range(9)]
    boxs_sum = [set() for _ in range(9)]

    row, col = len(board), len(board[0])

    for r in range(row):
        for c in range(col):
            if board[r][c] != ".":
                if board[r][c] in rows_sum[r] or board[r][c] in cols_sum[c]: 
                    return False
                if board[r][c] in boxs_sum[r//3 + (c//3 * 3)]: 
                    return False

                rows_sum[r].add(board[r][c])
                cols_sum[c].add(board[r][c])
                boxs_sum[r//3 + (c//3 * 3)].add(board[r][c])            
        
    return True


valid = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def with_change(r, c, digit):
    board = [row[:] for row in valid]
    board[r][c] = digit
    return board


empty = [["."] * 9 for _ in range(9)]

run("is_valid_sudoku", is_valid_sudoku, [
    ((valid,), True),
    ((with_change(0, 2, "5"),), False),   # row 0 already has a 5
    ((with_change(8, 0, "5"),), False),   # column 0 already has a 5
    ((with_change(1, 1, "8"),), False),   # top-left box already has an 8 (row 2)
    ((with_change(4, 4, "5"),), True),    # 5 is legal in the center
    ((empty,), True),
    ((with_change(8, 8, "1"),), False),   # column 8 already has a 1
])
