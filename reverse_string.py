# Reverse String (LeetCode #344) — two pointers, in place, O(n) time / O(1) space.

def reverse_string(chars):
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars


cases = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["a"], ["a"]),
    ([], []),
    (["a", "b"], ["b", "a"]),
    (["1", "2", "3", "4"], ["4", "3", "2", "1"]),
]

all_pass = True
for chars, expected in cases:
    work = list(chars)
    reverse_string(work)
    ok = work == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  reverse_string({chars}) -> {work}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
