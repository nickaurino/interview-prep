# Best Time to Buy and Sell Stock (LeetCode #121) — one-pass running best, O(n).
# Max profit from buying one day and selling a later day; 0 if no profit is possible.

def max_profit(prices):
    min_price = float("inf")
    best = 0
    for n in prices:
        if n < min_price:
            min_price = n
        else:
            best = max(best, n - min_price)
    return best


cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([], 0),
    ([5], 0),
    ([1, 2, 3, 4, 5], 4),
    ([2, 4, 1], 2),
    ([3, 3, 3], 0),
]

all_pass = True
for prices, expected in cases:
    got = max_profit(prices)
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  max_profit({prices}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
