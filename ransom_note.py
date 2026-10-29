from harness import run
from collections import Counter

# Ransom Note (LeetCode #383): Counter the magazine, then spend one letter per note letter.
# O(n + m) time, O(1) space for lowercase letters (at most 26 counts).


def can_construct(ransom_note, magazine):
    mag_dict = Counter(magazine)
    for char in ransom_note:
        if char in mag_dict:
            if mag_dict[char] <= 0:
                return False
            mag_dict[char] -= 1
        else:
            return False

    return True


run("can_construct", can_construct, [
    (("a", "b"), False),
    (("aa", "ab"), False),
    (("aa", "aab"), True),
    (("", "abc"), True),
    (("", ""), True),
    (("a", ""), False),
    (("abc", "cba"), True),
    (("aab", "baa"), True),
    (("aabb", "abab"), True),
    (("aabbb", "ababa"), False),
    (("hello", "lleoh"), True),
    (("hello", "helo"), False),
    (("zz", "zaz"), True),
])
