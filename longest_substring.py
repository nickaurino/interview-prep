from harness import run

# Longest Substring Without Repeating Characters (LeetCode #3) — sliding window, O(n).
# Return the length of the longest substring of s with no repeating character.


def length_of_longest(s):
    left = 0
    best = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        best = max(best, right - left + 1)
        seen.add(s[right])
    return best


run("length_of_longest", length_of_longest, [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("abcdef", 6),
    ("au", 2),
])
