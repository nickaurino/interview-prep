from harness import run

# Binary Tree Sum: return the sum of every value in a binary tree. Empty tree -> 0.
# Recursion (aggregate): this node's value + sum of the left subtree + sum of the right subtree.
# O(n) time, O(h) space for the call stack (h = tree height).


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_sum(node):
    sum = 0
    if node:
        sum += tree_sum(node.left)
        sum += tree_sum(node.right)
        sum += node.value
    return sum


#            1
#           / \
#          2   3
#         / \
#        4   5
t_full = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
t_one = TreeNode(5)
t_left = TreeNode(1, TreeNode(2, TreeNode(3)))
t_neg = TreeNode(-2, TreeNode(7), TreeNode(-5, None, TreeNode(1)))

run("tree_sum", tree_sum, [
    ((t_full,), 15),
    ((t_one,), 5),
    ((None,), 0),
    ((t_left,), 6),
    ((t_neg,), 1),
])
