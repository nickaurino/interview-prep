from harness import run

# Submatrix Pattern Match — slide a square pattern over a board of digits.
# A pattern cell that is a DIGIT must equal the board value; a pattern cell that is
# a LETTER maps 1:1 to a digit (same letter -> same digit, distinct letters ->
# distinct digits). Combines submatrix sliding with a letter<->digit bijection.
# Returns the top-left [row, col] (lowest row, then col) or [-1, -1].


def find_pattern(board, pattern):
    row, col = len(board), len(board[0])
    row_p, col_p = len(pattern), len(pattern[0])

    def submatrix(row, col):
        c_to_d = {}
        d_to_c = {}
        for r in range(row_p):
            for c in range(col_p):
                if pattern[r][c] in "0123456789":
                    if int(pattern[r][c]) != board[r + row][c + col]:
                        return False
                else:
                    if pattern[r][c] in c_to_d:
                        if c_to_d[pattern[r][c]] != int(board[r + row][c + col]):
                            return False
                    elif int(board[r + row][c + col]) in d_to_c:
                        if d_to_c[board[r + row][c + col]] != pattern[r][c]:
                            return False
                    else:
                        c_to_d[pattern[r][c]] = int(board[r + row][c + col])
                        d_to_c[int(board[r + row][c + col])] = pattern[r][c]
        return True

    for r in range(row - row_p + 1):
        for c in range(col - col_p + 1):
            if pattern[0][0] in "0123456789":
                if board[r][c] == int(pattern[0][0]):
                    if submatrix(r, c):
                        return [r, c]
            else:
                if submatrix(r, c):
                    return [r, c]
    return [-1, -1]


board_a = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

run("find_pattern", find_pattern, [
    ((board_a, [["5", "6"], ["8", "9"]]), [1, 1]),
    (([[1, 2, 3], [2, 1, 6], [7, 8, 9]], [["a", "b"], ["b", "a"]]), [0, 0]),
    (([[5, 5, 1], [5, 5, 1], [1, 1, 1]], [["a", "a"], ["a", "a"]]), [0, 0]),
    (([[7, 7], [7, 7]], [["a", "b"], ["a", "b"]]), [-1, -1]),
    (([[1, 2], [1, 4]], [["a", "2"], ["a", "4"]]), [0, 0]),
    ((board_a, [["9", "9"], ["9", "9"]]), [-1, -1]),
    ((board_a, [["a"]]), [0, 0]),
    (([[5, 5], [5, 5]], [["5", "a"], ["5", "a"]]), [0, 0]),
])
