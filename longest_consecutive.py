from harness import run

# Longest Consecutive Sequence (LeetCode #128) — hash set + run-start guard.
# Put everything in a set for O(1) lookups. Only begin counting a run at its START — a number
# n where n-1 is NOT in the set — then walk n+1, n+2, ... upward. The guard is what keeps it
# O(n): each number is walked at most once, as part of exactly one run (never re-counted).


def longest_consecutive(nums):
    set_nums = set(nums)
    best = 0

    for n in set_nums:
        if n - 1 not in set_nums:
            length = 0
            while n + length in set_nums:
                length += 1
            best = max(best, length)

    return best


run("longest_consecutive", longest_consecutive, [
    (([100, 4, 200, 1, 3, 2],), 4),
    (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
    (([],), 0),
    (([1],), 1),
    (([1, 2, 0, 1],), 3),
    (([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],), 7),
])
