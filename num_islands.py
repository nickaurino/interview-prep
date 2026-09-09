from harness import run

# Number of Islands (LeetCode #200) — grid DFS (flood fill), O(rows * cols).
# grid of "1" (land) / "0" (water); count connected land blobs (4-directional).
# Sinks each island in place so it isn't recounted.


def num_islands(grid):
    count = 0
    row = len(grid)
    col = len(grid[0])

    def flood(r, c):
        if r >= row or c >= col or r < 0 or c < 0:
            return
        if grid[r][c] == 0:
            return
        grid[r][c] = 0
        flood(r + 1, c)
        flood(r, c + 1)
        flood(r - 1, c)
        flood(r, c - 1)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                count += 1
                flood(r, c)

    return count


run("num_islands", num_islands, [
    ([[1, 1, 0], [1, 0, 0], [0, 0, 1]], 2),
    ([[0, 0], [0, 0]], 0),
    ([[1, 1, 1], [1, 1, 1]], 1),
    ([[1, 0, 1, 0, 1]], 3),
    ([[1]], 1),
    ([[1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 0]], 4),
])
