"""
Link: https://open.kattis.com/contests/ij53b6/problems/flyingsafely
"""

import sys
from collections import deque
from typing import Optional

DEBUG = True

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

        n, m = get_ints()

        known = set()
        result = 0
        # O(m)
        for _ in range(m):
            _, _ = get_ints()
        print(n - 1)


if __name__ == "__main__":
    main()
