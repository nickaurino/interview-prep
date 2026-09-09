# Valid Parentheses (LeetCode #20) — stack (LIFO), O(n).
# True if the brackets in s are properly matched and nested.

def is_valid(s):
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        else:
            if not stack:
                return False
            if stack.pop() != pair[c]:
                return False
    return not stack


cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("(", False),
    ("]", False),
    ("((()))", True),
]

all_pass = True
for s, expected in cases:
    got = is_valid(s)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  is_valid({s!r}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
