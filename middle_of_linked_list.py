# Middle of the Linked List (LeetCode #876) — fast & slow pointers, O(n) time / O(1) space.
# Return the middle node; for even length, return the second middle.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def build(values):
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head


cases = [
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 3),
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30, 40, 50, 60], 40),
]

all_pass = True
for values, expected in cases:
    node = find_middle(build(values))
    got = node.value if node else None
    ok = got == expected
    all_pass = all_pass and ok
    print(f"{'PASS' if ok else 'FAIL'}  find_middle({values}) -> {got}   expected {expected}")

print("\nALL TESTS PASSED" if all_pass else "\nSOME TESTS FAILED")
