from harness import run

# Top K Frequent Elements (LeetCode #347) — hashmap count + sort by count.
# Count each number, then sort the numbers by their count (descending) and take the top k.
# O(n log n) time (the sort), O(n) space. Optimal would swap the sort for a heap -> O(n log k).
from collections import defaultdict


def top_k_frequent(nums, k):
    counts = defaultdict(int)
    for n in nums:
        counts[n] += 1
    ranked = sorted(counts, key=lambda num: counts[num], reverse=True)
    return ranked[:k]


def _normalize(result):
    return sorted(result)   # any order is valid, so compare sorted


def solve(nums, k):
    return _normalize(top_k_frequent(nums, k))


run("solve", solve, [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1, 2], 2), [1, 2]),
    (([4, 4, 4, 5, 5, 6], 2), [4, 5]),
    (([5, 5, 5, 6, 6, 7, 7, 7, 7], 2), [5, 7]),
])
