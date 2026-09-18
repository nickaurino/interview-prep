import heapq
from harness import run

# Last Stone Weight (LeetCode #1046) — max-heap via negation.
# Each turn smash the two heaviest stones; if unequal, the difference goes back.
# heapq is min-only, so store negatives to simulate a max-heap.
# O(n log n) time, O(n) space.


def last_stone_weight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        a = -heapq.heappop(stones)   # biggest
        b = -heapq.heappop(stones)   # 2nd biggest
        if a != b:
            heapq.heappush(stones, -(a - b))
    return -stones[0] if stones else 0


run("last_stone_weight", last_stone_weight, [
    (([2, 7, 4, 1, 8, 1],), 1),
    (([1],), 1),
    (([1, 1],), 0),
    (([10, 4, 3, 2],), 1),
    (([3, 7, 2],), 2),
    (([31, 26, 33, 21, 40],), 9),
])
