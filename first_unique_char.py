from harness import run
from collections import Counter

# First Unique Character in a String (LeetCode #387) — hashing (Counter).
# Pass 1 counts every letter; pass 2 walks the STRING (not the Counter) so we can return an index.
# O(n) time, O(1) space (at most 26 lowercase keys).


def first_uniq_char(s):
    letter_freq = Counter(s)

    for i, char in enumerate(s):
        if letter_freq[char] == 1:
            return i

    return -1


run("first_uniq_char", first_uniq_char, [
    (("leetcode",), 0),
    (("loveleetcode",), 2),
    (("aabb",), -1),
    (("",), -1),
    (("z",), 0),
    (("aabbc",), 4),
    (("abcabcd",), 6),
    (("dabcabc",), 0),
])
