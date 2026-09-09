# Reverse Linked List (LeetCode #206) — iterative pointer rewiring, O(n) time / O(1) space.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def build(values):
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [3, 2, 1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([7, 7, 8], [8, 7, 7]),
]

all_pass = True
for values, expected in cases:
    got = to_list(reverse(build(values)))
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  reverse({values}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
