from harness import run

# Is Subsequence (LeetCode #392) — two pointers.
# Walk t once with a pointer i into s; each time t's letter matches s[i], move i forward.
# s is a subsequence if i reaches the end of s.
# O(t) time, O(1) space.


def is_subsequence(s, t):
    i = 0

    for char in t:
        if i < len(s) and s[i] == char:
            i += 1

    return i == len(s)


run("is_subsequence", is_subsequence, [
    (("abc", "ahbgdc"), True),
    (("axc", "ahbgdc"), False),
    (("", "ahbgdc"), True),
    (("a", ""), False),
    (("", ""), True),
    (("aaa", "aa"), False),
    (("ace", "abcde"), True),
    (("aec", "abcde"), False),
])
