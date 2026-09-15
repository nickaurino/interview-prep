from harness import run

# Fizz Buzz (LeetCode #412) — string accumulator, O(n).
# Build the word by concatenation so divisible-by-15 falls out for free
# (no separate %15 branch); empty word means it was a plain number.


def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        result.append(word if word else str(i))
    return result


run("fizz_buzz", fizz_buzz, [
    ((3,), ["1", "2", "Fizz"]),
    ((5,), ["1", "2", "Fizz", "4", "Buzz"]),
    ((15,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
             "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    ((1,), ["1"]),
])
