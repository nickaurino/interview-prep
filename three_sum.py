from harness import run

# 3Sum (LeetCode #15) — sort + two-pointer.
# Sort, then fix each nums[i] and two-pointer the rest for a pair summing to -nums[i].
# Skip duplicate first-numbers (nums[i] == nums[i-1]) and skip duplicate lefts after a
# match, so no triplet is emitted twice — no need to dedup the result list afterward.
# O(n^2) time (outer loop x two-pointer scan), O(1) extra space aside from the output.


def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif total > target:
                right -= 1
            else:
                left += 1

    return result


def _normalize(result):
    return sorted([sorted(t) for t in result])


def solve(nums):
    return _normalize(three_sum(nums))


run("solve", solve, [
    (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    (([0, 1, 1],), []),
    (([0, 0, 0],), [[0, 0, 0]]),
    (([],), []),
    (([-2, 0, 1, 1, 2],), [[-2, 0, 2], [-2, 1, 1]]),
])
