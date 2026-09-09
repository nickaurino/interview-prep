from harness import run

# Count Complete Tree Nodes (LeetCode #222, general form) — recursion, O(n).
# Total number of nodes in the tree. Empty tree -> 0.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.right) + count_nodes(node.left)


t_full = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
t_one = TreeNode(9)
t_skew = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))

run("count_nodes", count_nodes, [
    (t_full, 5),
    (t_one, 1),
    (None, 0),
    (t_skew, 3),
])
