from harness import run

# Daily Temperatures (LeetCode #739) — monotonic (decreasing) stack of indices.
# For each day, return how many days until a warmer temperature (0 if none).
# Keep a stack of indices still waiting for a warmer day; when today is warmer than the
# temp at the stack top, that day's answer is resolved as the index gap. Store INDICES, not
# temps, because the answer is the distance. Each index is pushed and popped once → O(n).


def daily_temperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            popped = stack.pop()
            result[popped] = i - popped
        stack.append(i)

    return result


run("daily_temperatures", daily_temperatures, [
    (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
    (([30, 40, 50, 60],), [1, 1, 1, 0]),
    (([30, 60, 90],), [1, 1, 0]),
    (([90, 60, 30],), [0, 0, 0]),
    (([50],), [0]),
    (([50, 50, 50],), [0, 0, 0]),
])
