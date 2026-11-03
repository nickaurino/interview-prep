from harness import run

# Missing Number (LeetCode #268): add up the indexes plus n to get what the sum should be,
# then subtract the real sum. What's left is the missing number.
# O(n) time, O(1) space.


def missing_number(nums):
    total_sum = 0
    nums_sum = 0
    for i, n in enumerate(nums):
        total_sum += i
        nums_sum += n

    return total_sum + len(nums) - nums_sum


run("missing_number", missing_number, [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([0], 1),
    ([1], 0),
    ([1, 2, 3], 0),
])
