from harness import run

# Maximum Sum of k Numbers in a Row (based on LeetCode #643) — sliding window.
# Seed the window with the first k, then slide: the new number enters, the one k back leaves.
# O(n) time, O(1) space.


def max_k_sum(nums, k):
    window = best = sum(nums[:k])

    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        best = max(window, best)
    return best


run("max_k_sum", max_k_sum, [
    (([1, 12, -5, -6, 50, 3], 4), 51),
    (([5], 1), 5),
    (([-1, -2, -3], 2), -3),
    (([1, 2, 3, 4], 4), 10),
    (([3, -1, 4, -1, 5], 2), 4),
])
