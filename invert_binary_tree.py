from harness import run

# Invert Binary Tree (LeetCode #226) — recursion, O(n).
# Swap left/right child at every node; return the inverted root. Empty tree -> None.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def invert(node):
    if not node:
        return None
    node.left, node.right = node.right, node.left
    invert(node.left)
    invert(node.right)
    return node


def shape(n):
    return None if n is None else (n.value, shape(n.left), shape(n.right))


def solve(node):
    return shape(invert(node))


t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
inverted = (1, (3, None, None), (2, (5, None, None), (4, None, None)))

run("solve", solve, [
    (t, inverted),
    (TreeNode(7), (7, None, None)),
    (None, None),
])
