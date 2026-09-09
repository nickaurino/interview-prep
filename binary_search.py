from harness import run

# Binary Search (LeetCode #704) — O(log n).
# nums is sorted ascending; return the index of target, or -1 if absent.


def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


run("search", search, [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    (([5], 5), 0),
    (([5], -5), -1),
    (([], 3), -1),
    (([1, 2, 3, 4, 5], 1), 0),
    (([1, 2, 3, 4, 5], 5), 4),
])
