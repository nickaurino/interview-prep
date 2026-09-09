from harness import run

# Submatrix Search — find where a small square pattern grid sits exactly inside a
# larger board of digits. Returns [row, col] of the top-left match (lowest row,
# then col), or [-1, -1]. O(R * C * k^2) for a k x k pattern.


def find_submatrix(board, pattern):
    row = len(board)
    col = len(board[0])
    row_p = len(pattern)
    col_p = len(pattern[0])

    def pattern_check(row, col):
        for r in range(row_p):
            for c in range(col_p):
                if board[row + r][col + c] != pattern[r][c]:
                    return False
        return True

    for r in range(row - row_p + 1):
        for c in range(col - col_p + 1):
            if board[r][c] == pattern[0][0]:
                if pattern_check(r, c):
                    return [r, c]
    return [-1, -1]


board3 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

run("find_submatrix", find_submatrix, [
    ((board3, [[5, 6], [8, 9]]), [1, 1]),
    ((board3, [[1, 2], [4, 5]]), [0, 0]),
    ((board3, [[1, 1], [1, 1]]), [-1, -1]),
    (([[1, 2], [2, 1]], [[1]]), [0, 0]),
    ((board3, [[5]]), [1, 1]),
    (([[1, 2], [3, 4]], [[1, 2], [3, 4]]), [0, 0]),
])
