from harness import run

# Backspace String Compare (LeetCode #844) — two pointers from the back, O(1) space.
# Walk both strings backward; a helper skips over each '#' and the letters it deletes.
# After both skips: both ran out -> equal; only one ran out -> not equal; letters differ -> not equal.
# O(n + m) time, O(1) space. (Simpler alternative: type each string out with a list/stack, O(n + m) space.)


def backspace_compare(s, t):
    s_pointer = len(s) - 1
    t_pointer = len(t) - 1

    while s_pointer > -1 and t_pointer > -1:
        s_pointer = decrement_pointer_for_backspace(s, s_pointer)
        t_pointer = decrement_pointer_for_backspace(t, t_pointer)

        if s_pointer < 0 and t_pointer < 0:
            return True
        if s_pointer < 0 or t_pointer < 0:
            return False
        if s[s_pointer] != t[t_pointer]:
            return False

        t_pointer -= 1
        s_pointer -= 1

    if s_pointer < 0 and t_pointer >= 0:
        t_pointer = decrement_pointer_for_backspace(t, t_pointer)
    if t_pointer < 0 and s_pointer >= 0:
        s_pointer = decrement_pointer_for_backspace(s, s_pointer)

    return s_pointer < 0 and t_pointer < 0

def decrement_pointer_for_backspace(s, pointer):
    skip = 0
    while pointer > -1 and s[pointer] == "#":
        skip +=1
        pointer -=1
        while skip != 0 and pointer > -1 and s[pointer] != '#':
            skip -= 1
            pointer -= 1

    return pointer


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
