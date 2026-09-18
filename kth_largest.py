import heapq
from harness import run

# Kth Largest Element in an Array (LeetCode #215) — min-heap of size k.
# Push each number; if the heap grows past k, pop the smallest. You always keep
# the k largest seen so far, so heap[0] (the smallest of those) is the kth largest.
# O(n log k) time, O(k) space. (Assumes len(nums) >= k.)


def kth_largest(nums, k):
    h = []
    for n in nums:
        heapq.heappush(h, n)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]


run("kth_largest", kth_largest, [
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    (([1], 1), 1),
    (([7, 6, 5, 4, 3, 2, 1], 5), 3),
    (([2, 1], 2), 1),
])
