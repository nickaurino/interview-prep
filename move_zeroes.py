from harness import run

# Move Zeroes (LeetCode #283) — two pointers (read/write), O(n) time, O(1) space.
# Move all 0s to the end in place, keep the non-zeros in their original order.
# write cursor marks the next slot; swap each non-zero forward into it.


def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def _apply(nums):
    move_zeroes(nums)
    return nums


run("move_zeroes", _apply, [
    (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    (([0],), [0]),
    (([1, 2, 3],), [1, 2, 3]),
    (([0, 0, 1],), [1, 0, 0]),
    (([1, 0],), [1, 0]),
    (([0, 0, 0],), [0, 0, 0]),
    (([],), []),
])
