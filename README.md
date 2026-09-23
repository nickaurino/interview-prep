# Interview Prep — LeetCode Solutions

My Python solutions to LeetCode problems, worked from scratch, each with a small test harness.
Committing daily as I prep for new-grad SWE / MLE interviews.

## Running

```bash
python3 two_sum.py
```

Each file prints `PASS` / `FAIL` for its test cases (some via the shared `harness.py`).

## Solutions

### Arrays & Hashing
| Problem | # | Pattern | Complexity |
|---|---|---|---|
| Two Sum | 1 | hashmap | O(n) |
| Contains Duplicate | 217 | hash set | O(n) |
| Valid Anagram | 242 | hashmap counts | O(n) |
| Group Anagrams | 49 | hashmap group-by-key | O(n·k log k) |
| Isomorphic Strings | 205 | two-way hashmap (bijection) | O(n) |

### Two Pointers
| Problem | # | Complexity |
|---|---|---|
| Valid Palindrome | 125 | O(n) time, O(1) space |
| Two Sum II (sorted input) | 167 | O(n) |
| Reverse String | 344 | O(n) in place |
| Container With Most Water | 11 | O(n) time, O(1) space |
| Move Zeroes | 283 | read/write pointers, O(n) time, O(1) space |

### Sliding Window
| Problem | # | Complexity |
|---|---|---|
| Longest Substring Without Repeating Characters | 3 | O(n) |

### Stack
| Problem | # | Complexity |
|---|---|---|
| Valid Parentheses | 20 | O(n) |

### Binary Search
| Problem | # | Complexity |
|---|---|---|
| Binary Search | 704 | O(log n) |

### Linked List
| Problem | # | Complexity |
|---|---|---|
| Reverse Linked List | 206 | O(n) time, O(1) space |
| Middle of the Linked List | 876 | fast/slow, O(n) time, O(1) space |
| Linked List Cycle | 141 | Floyd's fast/slow, O(n) time, O(1) space |

### Trees
| Problem | # | Complexity |
|---|---|---|
| Maximum Depth of Binary Tree | 104 | O(n) |
| Count Tree Nodes | 222 | O(n) |
| Invert Binary Tree | 226 | O(n) |

### Graphs / Grid
| Problem | # | Pattern | Complexity |
|---|---|---|---|
| Number of Islands | 200 | grid DFS (flood fill) | O(rows·cols) |
| Max Area of Island | 695 | grid DFS (flood returns area) | O(rows·cols) |

### Intervals
| Problem | # | Complexity |
|---|---|---|
| Merge Intervals | 56 | O(n log n) |
| Insert Interval | 57 | three-phase sweep, O(n) |
| Byte-Range Chunks (incremental merge) | — | O(n² log n) |

### Backtracking
| Problem | # | Pattern | Complexity |
|---|---|---|---|
| Subsets | 78 | choose / explore / un-choose | O(n·2ⁿ) |

### Dynamic / Greedy
| Problem | # | Pattern | Complexity |
|---|---|---|---|
| Best Time to Buy and Sell Stock | 121 | one-pass running best | O(n) |
| Maximum Subarray | 53 | Kadane's (running best) | O(n) |

### Math / Simulation
| Problem | # | Complexity |
|---|---|---|
| Fizz Buzz | 412 | string accumulator, O(n) |

### Matrix
| Problem | # | Complexity |
|---|---|---|
| Submatrix Search | — | O(R·C·k²) |
| Submatrix Pattern Match (letter↔digit bijection) | — | O(R·C·k²) |
