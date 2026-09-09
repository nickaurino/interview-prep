from harness import run

# Group Anagrams (LeetCode #49) — hashmap, group by a computed key.
# Anagrams sort to the same string, so use the sorted word as the bucket key.


def group_anagrams(words):
    buckets = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in buckets:
            buckets[key] = []
        buckets[key].append(word)
    return list(buckets.values())


def _normalize(groups):
    return sorted(sorted(g) for g in groups)


def solve(words):
    return _normalize(group_anagrams(words))


run("solve", solve, [
    ((["eat", "tea", "tan", "ate", "nat", "bat"],),
     _normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
    ((["abc", "bca", "cab", "xyz", "zzy"],),
     _normalize([["abc", "bca", "cab"], ["xyz"], ["zzy"]])),
    ((["aab", "abb", "bba", "baa"],),
     _normalize([["aab", "baa"], ["abb", "bba"]])),
])
