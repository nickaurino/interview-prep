from harness import run

# Valid Palindrome (LeetCode #125) — two pointers, O(n) time / O(1) space.
# True if s reads the same both ways, considering only letters/digits, ignoring case.


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


run("is_palindrome", is_palindrome, [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    (("",), True),
    ((" ",), True),
    (("0P",), False),
    (("ab_a",), True),
])
