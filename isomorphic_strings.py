# Isomorphic Strings (LeetCode #205) — two-way hashmap (bijection), O(n).
# True if s maps to t by a consistent one-to-one substitution, both directions.

def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for a, b in zip(s, t):
        if a in s_to_t:
            if s_to_t[a] != b:
                return False
        if b in t_to_s:
            if t_to_s[b] != a:
                return False
        s_to_t[a] = b
        t_to_s[b] = a
    return True


cases = [
    (("egg", "add"), True),
    (("foo", "bar"), False),
    (("badc", "baba"), False),
    (("paper", "title"), True),
    (("ab", "aa"), False),
    (("a", "a"), True),
]

all_pass = True
for (s, t), expected in cases:
    got = is_isomorphic(s, t)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  is_isomorphic({s!r}, {t!r}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
