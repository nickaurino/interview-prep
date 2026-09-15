from harness import run

# Maximum Subarray (LeetCode #53) — Kadane's, O(n) time, O(1) space.
# Largest contiguous subarray sum. At each number, either start fresh or extend:
#   running = max(num, running + num);  best = max(best, running).


def max_subarray(nums):
    best = float('-inf')
    running = best
    for n in nums:
        running = max(n, running + n)
        best = max(best, running)
    return best


run("max_subarray", max_subarray, [
    (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    (([1],), 1),
    (([5, 4, -1, 7, 8],), 23),
    (([-1],), -1),
    (([-2, -1],), -1),
    (([-3, -2, -5],), -2),
])
