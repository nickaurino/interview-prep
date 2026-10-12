from harness import run
from collections import defaultdict

# Majority Element (LeetCode #169) — hashmap counting with an early exit.
# Count as you go and return the moment a count passes n / 2 (float, so no rounding traps).
# O(n) time (worst case the last copy is at the end), O(n) space.


def majority_element(nums):
    freq = defaultdict(int)
    n = len(nums) / 2

    for num in nums:
        freq[num] += 1
        if freq[num] > n:
            return num

    return -1


run("majority_element", majority_element, [
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
    (([7],), 7),
    (([5, 5],), 5),
    (([1, 2, 1, 2, 1],), 1),
    (([4, 4, 4, 9, 9],), 4),
    (([6, 1, 6, 2, 6, 3, 6],), 6),
    (([1, 1, 2, 2, 2],), 2),
    (([3, 3, 4, 4, 4, 4],), 4),
])
