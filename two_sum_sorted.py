# Two Sum II - Input Array Is Sorted (LeetCode #167) — two pointers, O(n).
# nums is sorted ascending; return the [i, j] indices of the pair adding to target.
# (LeetCode #167 wants 1-indexed -> return [left+1, right+1] there.)

def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left != right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
    return None


cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, 3, 4], 6, [0, 2]),
    ([-1, 0], -1, [0, 1]),
    ([1, 2, 3, 4, 4, 9, 56, 90], 8, [3, 4]),
    ([1, 3, 4, 5, 7, 11], 9, [2, 3]),
]

all_pass = True
for nums, target, expected in cases:
    got = two_sum_sorted(nums, target)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  two_sum_sorted({nums}, {target}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
