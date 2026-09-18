from harness import run

# Product of Array Except Self (LeetCode #238) — prefix x suffix, no division.
# result[i] = (product of everything LEFT of i) * (product of everything RIGHT of i).
# Pass 1 (L->R): store the running prefix product before i.
# Pass 2 (R->L): multiply in the running suffix product after i.
# O(n) time, O(1) extra space (output array doesn't count). Identity for a product is 1, not 0.


def product_except_self(nums):
    n = len(nums)
    result = []

    prefix = 1
    for i in range(n):
        result.append(prefix)
        prefix = nums[i] * prefix

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] = result[i] * suffix
        suffix = nums[i] * suffix

    return result


run("product_except_self", product_except_self, [
    (([1, 2, 3, 4],), [24, 12, 8, 6]),
    (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    (([2, 3],), [3, 2]),
    (([1, 1, 1],), [1, 1, 1]),
    (([5, 2],), [2, 5]),
])
