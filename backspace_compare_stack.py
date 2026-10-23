from harness import run
from collections import deque

# Backspace String Compare (LeetCode #844) - stack version.
# Type each string into a stack: a letter is pushed, '#' pops (if there is anything to pop). Then compare.
# O(n + m) time, O(n + m) space. (The two-pointer version in backspace_compare.py uses O(1) space.)


def backspace_compare(s, t):
    return delete_char(s) == delete_char(t)

def delete_char(s):
    text = deque()
    for char in s:
        if text and char == "#":
            text.pop()
        elif char != "#":
            text.append(char)
    return text


run("backspace_compare", backspace_compare, [
    (("ab#c", "ad#c"), True),
    (("ab##", "c#d#"), True),
    (("a#c", "b"), False),
    (("a##c", "#a#c"), True),
    (("", ""), True),
    (("###", ""), True),
    (("abc", "abc"), True),
    (("abc#", "ab"), True),
    (("bxj##tw", "bxo#j##tw"), True),
    (("a", "aa#a"), False),
    (("", "a#"), True),
    (("a", "#"), False),
    (("a#", ""), True),
    (("ab#", "a"), True),
    (("a##b", "b"), True),
    (("ab##c#d", "d"), True),
])
