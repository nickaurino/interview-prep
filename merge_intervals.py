from harness import run

# Merge Intervals (LeetCode #56) — sort + sweep, O(n log n).
# Given a list of [start, end] intervals, merge all overlapping ones.

def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda pair: pair[0])
    result = [intervals[0]]
    for n in intervals[1:]:
        if result[-1][1] >= n[0]:
            result[-1][1] = max(result[-1][1], n[1])
        else:
            result.append(n)
    return result


run("merge", merge, [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
    ([[5, 6], [1, 3], [2, 4]], [[1, 4], [5, 6]]),
    ([[1, 4]], [[1, 4]]),
])
