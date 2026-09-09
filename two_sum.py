# Two Sum (LeetCode #1) — hashmap, O(n) time / O(n) space.
# Return the indices of the two numbers that add up to target.

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return None


cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
]

all_pass = True
for nums, target, expected in cases:
    got = two_sum(nums, target)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  two_sum({nums}, {target}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
