from harness import run

# Majority Element (LeetCode #169) — O(1) space follow-up (Boyer-Moore voting).
# Each copy of the majority cancels against one different number. The majority outnumbers
# everything else combined, so the others run out first and it's the one left standing.
# O(n) time, O(1) space.


def majority_element(nums):
    candidate = count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


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
    (([9, 9, 1, 2, 9],), 9),
])
