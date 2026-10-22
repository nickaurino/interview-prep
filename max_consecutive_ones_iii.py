from harness import run

# Max Consecutive Ones III (LeetCode #1004) - variable-size sliding window.
# Right grows the window every step; left shrinks it while the window holds more than k zeros.
# O(n) time, O(1) space.


def longest_ones(nums, k):
    max_window = zeros = 0
    left = right = 0

    while right < len(nums):

        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        right += 1

        max_window = max(max_window, right - left)

    return max_window


run("longest_ones", longest_ones, [
    (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
    (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10),
    (([1, 1, 1], 0), 3),
    (([0, 0, 0], 0), 0),
    (([0, 0, 0], 2), 2),
    (([0, 0, 0], 5), 3),
    (([1], 0), 1),
    (([0], 1), 1),
    (([1, 0, 1, 0, 1], 1), 3),
    (([1, 0, 1, 0, 1], 0), 1),
    (([0, 1, 1, 0, 1, 1, 0], 1), 5),
    (([1, 1, 0, 0, 1, 1, 1, 0, 1], 1), 5),
    (([0, 1, 0, 0, 1, 1, 0, 1], 2), 5),
])
