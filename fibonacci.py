from harness import run

# Fibonacci Number (LeetCode #509) — bottom-up DP.
# Build the sequence up to n, each entry = the two before it, so nothing is recomputed.
# O(n) time, O(n) space (keeping only the last two would make it O(1)).


def fib(n):
    if n <= 1: return n
    fib_l = [0, 1]

    i = 2
    while i <= n:
        fib_l.append(fib_l[-1] + fib_l[-2])
        i += 1

    return fib_l[n]


run("fib", fib, [
    ((0,), 0),
    ((1,), 1),
    ((2,), 1),
    ((3,), 2),
    ((4,), 3),
    ((5,), 5),
    ((10,), 55),
    ((20,), 6765),
])
