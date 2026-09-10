from harness import run

# Max Area of Island (LeetCode #695) — grid DFS (flood fill), O(rows * cols).
# grid of 1 (land) / 0 (water); return the area of the largest island (4-directional).
# The flood returns the island's size (1 + the four neighbor floods); track the max.
# Sinks each island in place so it isn't recounted.


def max_area_of_island(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    best = 0

    def island_area(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + island_area(r + 1, c) + island_area(r - 1, c) + island_area(r, c + 1) + island_area(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                best = max(island_area(r, c), best)

    return best


run("max_area_of_island", max_area_of_island, [
    ([[1, 1, 0], [1, 0, 0], [0, 0, 1]], 3),
    ([], 0),
    ([[0, 0], [0, 0]], 0),
    ([[1, 1], [1, 1]], 4),
    ([[1, 0], [0, 1]], 1),
    ([[1]], 1),
    ([[1, 0, 0], [0, 1, 1], [0, 1, 1]], 4),
])
