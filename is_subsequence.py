from harness import run

# Is Subsequence (LeetCode #392) — two pointers.
# Walk t once, keeping a count of how many letters of s are matched so far.
# The slice s[count:count+1] returns "" past the end instead of raising an IndexError.
# O(t) time, O(1) space.


def is_subsequence(s, t):
    if s == "": return True

    next_char = s[0:1]
    count = 0

    for char in t:
        if char == next_char:
            count += 1
            next_char = s[count:count+1]
        if count == len(s):
            return True

    return False


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
