from harness import run

# Lemonade Change (LeetCode #860) — greedy.
# Track bill COUNTS, not a dollar total: $15 in change can need specific bills.
# For a $20, give $10 + $5 first: a $5 can make change for both a $10 and a $20, a $10 only for a $20.
# O(n) time, O(1) space.


def lemonade_change(bills):
    fives = tens = 0

    for b in bills:
        if b == 10:
            if not fives:
                return False
            fives -= 1
            tens += 1
        elif b == 20:
            if fives and tens:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
        elif b == 5:
            fives += 1

    return True


run("lemonade_change", lemonade_change, [
    (([5, 5, 5, 10, 20],), True),
    (([5, 5, 10, 10, 20],), False),
    (([10],), False),
    (([5, 5, 10],), True),
    (([5, 5, 5, 20],), True),
    (([5, 5, 5, 5, 20, 20],), False),
    (([5, 10, 5, 20],), True),
    (([5, 5, 5, 5, 10, 20, 10],), True),
    (([],), True),
])
