import random
from collections import Counter

# Shuffle an Array (LeetCode #384) — Fisher-Yates, in place.
# Walk backward; swap each slot with a random pick from the still-unshuffled zone [0..i].
# Picking WITHOUT replacement gives n! equally likely paths, one per ordering → perfectly fair.
# O(n) time, O(1) extra space.


def shuffle(nums):
    last = len(nums) - 1
    for i in range(last):
        rand = random.randint(0, (last - i))
        nums[rand], nums[last - i] = nums[last - i], nums[rand]

    return nums


# Randomness can't be checked against one expected answer, so test properties + uniformity.
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    return ok


results = []
original = [1, 2, 3, 4, 5]
nums = original[:]
results.append(check("shuffles in place", shuffle(nums) is nums))
results.append(check("keeps every element", sorted(nums) == original))
results.append(check("empty list", shuffle([]) == []))
results.append(check("single element", shuffle([7]) == [7]))

TRIALS = 60000
counts = Counter(tuple(shuffle([1, 2, 3])) for _ in range(TRIALS))
worst = max(abs(c - TRIALS / 6) / (TRIALS / 6) for c in counts.values())
results.append(check("all 6 orderings appear", len(counts) == 6))
results.append(check("uniform within 5%", worst < 0.05, f"worst deviation {worst:.1%}"))

print("\nALL PASSED ✅" if all(results) else "\nSOME FAILED ❌")
