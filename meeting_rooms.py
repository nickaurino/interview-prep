from harness import run

# Meeting Rooms (LeetCode #252) — intervals.
# Sort by start time, then each meeting only needs to end before the next one starts.
# Strict > so back-to-back meetings ([1,5], [5,10]) don't count as overlapping.
# O(n log n) time (the sort dominates), O(n) space for the sorted copy.


def can_attend_meetings(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    for i in range(len(sorted_intervals) - 1):
        if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
            return False

    return True


run("can_attend_meetings", can_attend_meetings, [
    (([[0, 30], [5, 10], [15, 20]],), False),
    (([[7, 10], [2, 4]],), True),
    (([],), True),
    (([[5, 8]],), True),
    (([[1, 5], [5, 10]],), True),
    (([[1, 5], [4, 10]],), False),
    (([[9, 12], [1, 3], [3, 6], [6, 9]],), True),
    (([[1, 10], [2, 3], [11, 12]],), False),
])
