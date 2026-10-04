from harness import run

# Search Insert Position (LeetCode #35) — binary search.
# Sorted nums + target. Return the index if found, else the index where it would be inserted.
# Standard binary search; when not found, the left pointer lands on the insertion point.
# Big-O: O(log n) time, O(1) space.


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

run("search_insert", search_insert, [
    (([1, 3, 5, 6], 5), 2),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
    (([1, 3, 5, 6], 0), 0),
    (([1], 0), 0),
    (([1], 2), 1),
    (([1, 3], 3), 1),
])
