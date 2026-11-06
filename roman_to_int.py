from harness import run

# Roman to Integer (LeetCode #13): walk the numeral right to left. Add a symbol unless it is
# smaller than the symbol to its right, then subtract it (the "IV" = 4 case).
# O(n) time, O(1) space.


def roman_to_int(s):
    roman_dict = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    total = 0
    prev = 1
    for i in range(len(s) - 1, -1, -1):
        if roman_dict[s[i]] >= prev:
            total += roman_dict[s[i]]
        else:
            total -= roman_dict[s[i]]
        prev = roman_dict[s[i]]

    return total


run("roman_to_int", roman_to_int, [
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("XL", 40),
    ("MMXXVI", 2026),
])
