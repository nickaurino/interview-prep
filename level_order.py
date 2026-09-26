from harness import run

# Binary Tree Level Order Traversal (LeetCode #102) — BFS.
# Process the tree one level at a time: drain the current level, collecting its values,
# while queueing each node's children as the next level. O(n) time, O(n) space
# (the queue holds up to one full level, the widest of which is ~n/2 nodes).


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root):
    if not root: return []
    queue = [root]
    result = []
    
    while queue:
        level = []
        temp_queue = []
        while queue:
            popped = queue.pop(0)
            level.append(popped.value)
            if popped.left:
                temp_queue.append(popped.left)
            if popped.right:
                temp_queue.append(popped.right)

        result.append(level)
        queue = temp_queue

    return result
        


t_example = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t_single = TreeNode(1)
t_left_skew = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
t_full = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
t_gappy = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))

run("level_order", level_order, [
    ((t_example,), [[3], [9, 20], [15, 7]]),
    ((None,), []),
    ((t_single,), [[1]]),
    ((t_left_skew,), [[1], [2], [3], [4]]),
    ((t_full,), [[1], [2, 3], [4, 5, 6, 7]]),
    ((t_gappy,), [[1], [2, 3], [4, 5]]),
])
