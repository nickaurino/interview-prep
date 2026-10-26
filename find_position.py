from harness import run

# Find Position: return [row, col] of the first time target appears in a grid
# (row by row, left to right), or [-1, -1] if it isn't there.
# O(R*C) time, O(1) space.


def find_position(grid, target):
    for i, row in enumerate(grid):
        for i2, element in enumerate(row):
            if element == target:
                return[i, i2]
    return [-1, -1]


run("find_position", find_position, [
    (([[1, 2, 3], [4, 5, 6]], 5), [1, 1]),
    (([[7, 2], [0, 4], [9, 1]], 9), [2, 0]),
    (([[1, 2], [3, 1]], 1), [0, 0]),   # first hit = row 0, col 0 (not the later one)
    (([[1, 2], [3, 4]], 9), [-1, -1]),  # not found
    (([[5]], 5), [0, 0]),
])
