"""Reusable test runner for every code rep. Keeps rep files tiny + token-light.

Rep file pattern (that's the WHOLE file):
    from harness import run
    def solve(nums, target):
        ...
    run("solve", solve, [
        ((nums, target), expected),   # args as a tuple, then expected
        (("abc",), 3),                # single arg still needs the trailing comma
    ])
"""


def run(name, fn, cases):
    all_pass = True
    for args, expected in cases:
        args_t = args if isinstance(args, tuple) else (args,)
        got = fn(*args_t)
        ok = got == expected
        all_pass = all_pass and ok
        shown = ", ".join(repr(a) for a in args_t)
        print(f"{'PASS' if ok else 'FAIL'}  {name}({shown}) -> {got!r}   expected {expected!r}")
    print("\nALL PASSED ✅" if all_pass else "\nSOME FAILED ❌")
    return all_pass
