from harness import run

# Robot Return to Origin (LeetCode #657): one counter for up/down, one for left/right.
# The robot is home only if both counters end at zero.
# O(n) time, O(1) space.


def judge_circle(moves):
    left_right = up_down = 0
    for m in moves:
        if m == "U":
            up_down += 1
        elif m == "D":
            up_down -= 1
        elif m == "L":
            left_right += 1
        elif m == "R":
            left_right -= 1

    return left_right == 0 and up_down == 0


run("judge_circle", judge_circle, [
    ("UD", True),
    ("LL", False),
    ("RRDDLLUU", True),
    ("", True),
    ("U", False),
    ("UDLRL", False),
    ("LDRRLRUULR", False),
])
