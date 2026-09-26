from harness import run

# Permutations (LeetCode #46) — backtracking.
# Fill one slot per call: loop over every number, skip any already in the path, then
# choose (append) → explore (recurse) → un-choose (pop). A full path is one ordering.
# n! orderings, each copied in O(n) → O(n · n!) time; O(n) recursion depth (excluding output).


def permute(nums):
    result = []

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for n in nums:
            if n in path:
                continue
            path.append(n)
            backtrack(path)
            path.pop()

    backtrack([])
    return result


def solve(nums):
    return sorted(permute(nums))


run("solve", solve, [
    (([1, 2, 3],), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    (([0, 1],), [[0, 1], [1, 0]]),
    (([1],), [[1]]),
])
