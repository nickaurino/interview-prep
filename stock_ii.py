from harness import run

# Best Time to Buy and Sell Stock II (LeetCode #122) — greedy.
# Any climb equals the sum of its daily steps, so take every positive day-to-day difference.
# O(n) time. The prices[1:] slice copies the list, so O(n) space (an index loop would be O(1)).


def max_profit(prices):
    return sum(max(p - prices[i-1], 0) for i, p in enumerate(prices[1:], start=1))


run("max_profit", max_profit, [
    (([7, 1, 5, 3, 6, 4],), 7),
    (([1, 2, 3, 4, 5],), 4),
    (([7, 6, 4, 3, 1],), 0),
    (([5],), 0),
    (([],), 0),
    (([1, 5, 1, 5],), 8),
    (([3, 3, 3],), 0),
])
