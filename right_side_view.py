from collections import deque

from harness import run

# Binary Tree Right Side View (LeetCode #199) — BFS.
# Level-order traversal, left child before right, so the last node drained from each
# level is the rightmost one visible. O(n) time, O(n) space.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def right_side_view(root):
    if root is None: return []

    q = deque([root])
    result = []


    while q:
        temp_q = deque()

        while q:
            node = q.popleft()
            if node.left is not None:
                temp_q.append(node.left)
            if node.right is not None:
                temp_q.append(node.right)
        
        result.append(node.value)
        q = temp_q

    return result
            
    



t_example = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
t_left_only = TreeNode(1, TreeNode(2))
t_single = TreeNode(7)
t_deep_left = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3))
t_full = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

run("right_side_view", right_side_view, [
    ((t_example,), [1, 3, 4]),
    ((t_left_only,), [1, 2]),
    ((None,), []),
    ((t_single,), [7]),
    ((t_deep_left,), [1, 3, 4, 6]),
    ((t_full,), [1, 3, 7]),
])
