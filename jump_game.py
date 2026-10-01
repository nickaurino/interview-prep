from harness import run

# Jump Game (LeetCode #55) — greedy.
# Walk backwards keeping a goal index; if index i can reach the goal, i becomes the new goal.
# Reachable iff the goal makes it back to index 0. O(n) time, O(1) space.


def can_jump(nums):
    goal = len(nums) - 1
    
    for i in range(len(nums) -2, -1, -1):
        if nums[i] + i  >= goal:
            goal = i

    return goal == 0


run("can_jump", can_jump, [
    (([2, 3, 1, 1, 4],), True),
    (([3, 2, 1, 0, 4],), False),
    (([0],), True),
    (([1, 0],), True),
    (([0, 1],), False),
    (([2, 0, 0],), True),
    (([1, 1, 0, 1],), False),
    (([5, 0, 0, 0, 0, 0],), True),
    (([2, 5, 0, 0],), True),
    (([1, 2, 0, 0, 1],), False),
])
