from harness import run

# Contains Duplicate II (LeetCode #219) — sliding window + set.
# Only look BACK: every matching pair is caught once, when its later element arrives.
# The set holds the k numbers right behind i; the one k steps back leaves as the new one enters.
# O(n) time, O(k) space.


def contains_nearby_duplicate(nums, k):
    if k == 0: return False

    window = set()
    for n in nums[:k]:
        if n in window:
            return True
        window.add(n)

    for i in range(k, len(nums)):
        if nums[i] in window:
            return True
        window.remove(nums[i-k])
        window.add(nums[i])

    return False


run("contains_nearby_duplicate", contains_nearby_duplicate, [
    (([1, 2, 3, 1], 3), True),
    (([1, 0, 1, 1], 1), True),
    (([1, 2, 3, 1, 2, 3], 2), False),
    (([], 0), False),
    (([1, 1], 0), False),
    (([99, 99], 2), True),
    (([1, 2, 1], 1), False),
    (([4, 1, 2, 3, 1, 5, 4], 3), True),
])
