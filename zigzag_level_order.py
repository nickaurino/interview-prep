from harness import run
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Binary Tree Zigzag Level Order Traversal (LeetCode #103) — BFS.
# Walk each level left-to-right as usual, then reverse every other finished row.
# O(n) time, O(n) space.


def zigzag(root):
    if root is None: return []

    is_left = True
    q = deque()
    q.append(root)
    result = []

    while q:
        next_line = deque()
        line_values = []

        while q:
            node = q.popleft()
            line_values.append(node.value)

        
            if not node.left is None:
                next_line.append(node.left) 
            if not node.right is None:
                next_line.append(node.right)

        if is_left: result.append(line_values)
        else: result.append(line_values[::-1])

        is_left = not is_left
        q = next_line

    return result
            


t_example = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t_full = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
t_single = TreeNode(7)
t_deep_left = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3))
t_four = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)),
                  TreeNode(3, TreeNode(6), TreeNode(7)))

run("zigzag", zigzag, [
    ((t_example,), [[3], [20, 9], [15, 7]]),
    ((t_full,), [[1], [3, 2], [4, 5, 6, 7]]),
    ((None,), []),
    ((t_single,), [[7]]),
    ((t_deep_left,), [[1], [3, 2], [4], [6]]),
    ((t_four,), [[1], [3, 2], [4, 5, 6, 7], [9, 8]]),
])
