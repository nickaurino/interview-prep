from harness import run

# Leaderboard ranking — custom sort key.
# Rank names by score (highest first), breaking ties alphabetically, in ONE sort:
# a tuple key compares score first, then name; negating the score makes the biggest
# score sort first without reverse=True (which would flip the names too).
# O(n log n) time, O(n) space.


def leaderboard(players):

    sorted_players = sorted(players, key= lambda p: (-p[1], p[0]))

    return [p[0] for p in sorted_players]


run("leaderboard", leaderboard, [
    (([("zoe", 90), ("amy", 75), ("bob", 90)],), ["bob", "zoe", "amy"]),
    (([],), []),
    (([("solo", 10)],), ["solo"]),
    (([("c", 5), ("b", 5), ("a", 5)],), ["a", "b", "c"]),
    (([("x", -3), ("y", 0), ("w", -3)],), ["y", "w", "x"]),
    (([("kai", 100), ("ana", 20), ("lee", 100), ("bo", 55), ("al", 20)],), ["kai", "lee", "bo", "al", "ana"]),
])
