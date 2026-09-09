from harness import run

# Byte-Range Chunks — merge intervals, run incrementally.
# Ranges arrive one at a time; after each arrives, report the merged set of ranges
# so far. Adjacent ranges merge (e.g. [1,1] and [2,2] -> [1,2]).


def merge(intervals):
    if not intervals:
        return []
    intervals_s = sorted(intervals, key=lambda pair: pair[0])
    result = [list(intervals_s[0])]
    for n in intervals_s:
        if result[-1][1] + 1 >= n[0]:
            result[-1][1] = max(result[-1][1], n[1])
        else:
            result.append(list(n))
    return result


def byte_ranges(chunks):
    seen = []
    result = []
    for n in chunks:
        seen.append(n)
        result.append(merge(seen))
    return result


run("byte_ranges", byte_ranges, [
    ([[1, 1], [2, 2], [3, 3]], [[[1, 1]], [[1, 2]], [[1, 3]]]),
    ([[1, 3], [2, 6], [8, 10]], [[[1, 3]], [[1, 6]], [[1, 6], [8, 10]]]),
    ([[1, 2], [5, 6], [3, 4]], [[[1, 2]], [[1, 2], [5, 6]], [[1, 6]]]),
    ([[1, 5], [2, 3]], [[[1, 5]], [[1, 5]]]),
    ([[4, 4]], [[[4, 4]]]),
    ([[1, 2], [1, 2]], [[[1, 2]], [[1, 2]]]),
])
