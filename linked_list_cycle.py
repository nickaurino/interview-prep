from harness import run

# Linked List Cycle (LeetCode #141) — Floyd's fast/slow, O(n) time, O(1) space.
# Return True if the list has a cycle. Cycle -> fast and slow collide;
# no cycle -> fast reaches the end (None).


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def build_cycle(vals, pos):
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0 and nodes:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


run("has_cycle", lambda vals, pos: has_cycle(build_cycle(vals, pos)), [
    (([3, 2, 0, -4], 1), True),
    (([1, 2], 0), True),
    (([1], 0), True),
    (([1], -1), False),
    (([], -1), False),
    (([1, 2, 3, 4], -1), False),
])
