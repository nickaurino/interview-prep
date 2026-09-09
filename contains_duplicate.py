# Contains Duplicate (LeetCode #217) — hash set, O(n).
# True if any value appears more than once.

def has_duplicates(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


cases = [
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 1], True),
    ([], False),
    ([7], False),
    ([5, 5], True),
    ([9, 8, 7, 8], True),
]

all_pass = True
for nums, expected in cases:
    got = has_duplicates(nums)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  has_duplicates({nums}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
