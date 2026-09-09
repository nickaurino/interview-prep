# Valid Anagram (LeetCode #242) — hashmap letter counts, O(n).
# True if t is an anagram of s (same letters, same counts).

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    dict_s = {}
    dict_t = {}
    for c in s:
        dict_s[c] = dict_s.get(c, 0) + 1
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1

    return dict_s == dict_t


cases = [
    ("listen", "silent", True),
    ("rat", "car", False),
    ("anagram", "nagaram", True),
    ("a", "ab", False),
    ("", "", True),
    ("aabb", "bbaa", True),
    ("aabb", "abbb", False),
]

all_pass = True
for s, t, expected in cases:
    got = is_anagram(s, t)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  is_anagram({s!r}, {t!r}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
