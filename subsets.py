from harness import run

# Subsets (LeetCode #78) — backtracking (choose / explore / un-choose).
# Walk an index i through nums; at each element make a binary choice: include nums[i] or skip it.
# When i reaches the end, one complete walk is a finished subset — record a COPY (path[:]) so later
# mutations don't clobber it. Un-choose (path.pop()) after exploring the "include" branch so the
# "skip" branch starts clean. 2^n subsets total.
# O(n * 2^n) time, O(n) recursion depth (excluding the output).


def subsets(nums):
    result = []

    def backtrack(i, path):
        if i == len(nums):
            result.append(path[:])
            return
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
        backtrack(i + 1, path)

    backtrack(0, [])
    return result


def _normalize(result):
    return sorted([sorted(s) for s in result])


def solve(nums):
    return _normalize(subsets(nums))


run("solve", solve, [
    (([1, 2, 3],), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
    (([0],), [[], [0]]),
    (([],), [[]]),
    (([1, 2],), [[], [1], [1, 2], [2]]),
])
