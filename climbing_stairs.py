from harness import run

# Climbing Stairs (LeetCode #70) — DP (secretly Fibonacci).
# To reach step n, the last move was a 1-step (from n-1) or a 2-step (from n-2),
# so ways(n) = ways(n-1) + ways(n-2). Roll two variables to keep space O(1).
# O(n) time, O(1) space.


def climbing_stairs(n):
    if n <= 2:
        return n
    one_back, two_back = 2, 1
    result = 0
    for _ in range(2, n):
        result = one_back + two_back
        two_back = one_back
        one_back = result
    return result


run("climbing_stairs", climbing_stairs, [
    ((1,), 1),
    ((2,), 2),
    ((3,), 3),
    ((4,), 5),
    ((5,), 8),
    ((6,), 13),
    ((10,), 89),
])
