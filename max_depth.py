from harness import run

# Maximum Depth of Binary Tree (LeetCode #104) — recursion, O(n).
# Depth = number of nodes on the longest root-to-leaf path. Empty tree -> 0.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.right), max_depth(node.left))


t_bal = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
t_one = TreeNode(5)
t_skew = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))

run("max_depth", max_depth, [
    (t_bal, 3),
    (t_one, 1),
    (None, 0),
    (t_skew, 3),
])
