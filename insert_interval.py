from harness import run

# Insert Interval (LeetCode #57) — three-phase sweep, O(n) time, O(n) space.
# intervals are sorted by start & non-overlapping; insert `new`, merging overlaps.
#   1) append intervals ending before new starts
#   2) merge overlapping intervals into new, then append new
#   3) append the rest


def insert_interval(intervals, new):
    result = []
    i = 0
    while i < len(intervals) and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= new[1]:
        new = [min(intervals[i][0], new[0]), max(intervals[i][1], new[1])]
        i += 1
    result.append(new)
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    return result


run("insert_interval", insert_interval, [
    (([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
    (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]]),
    (([], [5, 7]), [[5, 7]]),
    (([[3, 5]], [1, 2]), [[1, 2], [3, 5]]),
    (([[1, 2]], [3, 4]), [[1, 2], [3, 4]]),
    (([[2, 3], [5, 7]], [1, 10]), [[1, 10]]),
])
