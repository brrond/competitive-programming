"""
Link: https://codeforces.com/contest/2207/problem/A
"""

import sys

DEBUG = False

input_file = None
if DEBUG:
    input_file = open("../input.txt", "r", encoding="utf-8")


def get_string() -> str:
    """Returns a string from the input."""

    if DEBUG and input_file is not None:
        line = input_file.readline()
    else:
        line = sys.stdin.readline()
    return line.strip()


def get_int() -> int:
    """Returns an integer from the input."""

    return int(get_string())


def get_ints() -> list[int]:
    """Returns integers from the input."""

    return list(map(int, get_string().split()))


def get_float() -> float:
    """Returns a float from the input."""

    return float(get_string())


def get_floats() -> list[float]:
    """Returns floats from the input."""

    return list(map(float, get_string().split()))


def main() -> None:
    """Solution goes here."""

    t = get_int()
    for _ in range(t):

        n = get_int()
        s = list(get_string())

        for i in range(1, n - 1):
            if s[i - 1] == s[i + 1] == "1":
                s[i] = "1"

        maximum = 0
        for el in s:
            if el == "1":
                maximum += 1

        for i in range(1, n - 1):
            if s[i - 1] == s[i + 1] == "1":
                s[i] = "0"

        minimum = 0
        for el in s:
            if el == "1":
                minimum += 1

        print(minimum, maximum)


if __name__ == "__main__":
    main()
