from harness import run

# Combinations (LeetCode #77) — backtracking.
# Choose / explore / un-choose, but each level only looks FORWARD (next start = i + 1),
# so every group is built once, smallest first. O(k · C(n, k)) time.


def combine(n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start,n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1,[])
            
    return result


def solve(n, k):
    return sorted(sorted(group) for group in combine(n, k))


run("solve", solve, [
    ((4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    ((1, 1), [[1]]),
    ((3, 3), [[1, 2, 3]]),
    ((3, 1), [[1], [2], [3]]),
    ((5, 3), [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5],
              [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]),
])
