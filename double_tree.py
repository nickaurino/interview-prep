from harness import run

# Double Every Node: multiply every value in a binary tree by 2, in place, and return the root.
# Recursion (transform mode): do this node's job, call both children as statements, return the node.
# O(n) time, O(h) space for the call stack.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def double(node):
    if not node: return None
    node.value = node.value * 2
    double(node.left)
    double(node.right)
    return node


def shape(n):
    return None if n is None else (n.value, shape(n.left), shape(n.right))


def solve(node):
    return shape(double(node))


#        1                    2
#       / \                  / \
#      2   3    double -->   4   6
#     / \                    / \
#    4   5                   8   10
t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
doubled = (2, (4, (8, None, None), (10, None, None)), (6, None, None))

run("solve", solve, [
    (t, doubled),
    (TreeNode(7), (14, None, None)),
    (None, None),
])
