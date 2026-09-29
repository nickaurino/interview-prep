from harness import run

# Reorder Data in Log Files (LeetCode #937) — custom sort key.
# One sort with a key function: letter-logs get (0, content, identifier) so they come first,
# sorted by content then identifier; every digit-log gets the SAME key (1,), so Python's
# stable sort keeps them in their original order. O(n log n · L) time for log length L, O(n) space.


def reorder_logs(logs):

    def sort_key(log):
        identifier, content = log.split(" ", 1)
    
        if content[0].isdigit():
            return(1, )
        else:
            return(0, content, identifier)

    return sorted(logs, key= sort_key)

run("reorder_logs", reorder_logs, [
    ((["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],),
     ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]),
    ((["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],),
     ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]),
    ((["let2 art can", "let1 art can"],), ["let1 art can", "let2 art can"]),
    ((["d3 5", "d1 9", "d2 1"],), ["d3 5", "d1 9", "d2 1"]),
    (([],), []),
])
