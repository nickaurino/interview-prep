from harness import run

# Unique Number of Occurrences (LeetCode #1207): count each number with a dict, then walk the counts
# with a "seen" set. A repeated count means the answer is False.
# O(n) time, O(n) space.


def unique_occurrences(arr):
    numbers_dict = {}
    for n in arr:
        if n in numbers_dict:
            numbers_dict[n] += 1
        else:
            numbers_dict[n] = 1

    values = set()
    for n in numbers_dict.values():
        if n in values:
            return False
        values.add(n)

    return True


run("unique_occurrences", unique_occurrences, [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ([5], True),
    ([4, 4, 4, 4], True),
    ([1, 1, 2, 2], False),
])
