from harness import run

# Container With Most Water (LeetCode #11) — two pointers, O(n) time / O(1) space.
# Area between two walls = min(height) * width; move the shorter wall inward.


def max_area(heights):
    left, right = 0, len(heights) - 1
    result = 0
    while left < right:
        result = max(result, min(heights[left], heights[right]) * (right - left))
        if heights[left] <= heights[right]:
            left += 1
        elif heights[left] >= heights[right]:
            right -= 1
    return result


run("max_area", max_area, [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    (([1, 1],), 1),
    (([4, 3, 2, 1, 4],), 16),
    (([1, 2, 1],), 2),
    (([5, 4, 3, 2, 1],), 6),
])
