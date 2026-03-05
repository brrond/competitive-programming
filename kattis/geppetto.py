"""
Link: https://open.kattis.com/problems/geppetto

3 2
1 2
2 3

5

All:
1, 2, 3
1 2, 2 3, 1 3
1 2 3

Possible:
[],
1, 2, 3
1 3



3 0

8

3 3
1 2
1 3
2 3

4

All:
1, 2, 3
"""

import sys
import itertools
from collections import defaultdict

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


def main():
    """Solution goes here."""

    n, m = get_ints()
    pairs = defaultdict(set)
    for _ in range(m):
        a, b = get_ints()
        pairs[a].add(b)
        pairs[b].add(a)

    def is_possible(arr: list[int]):
        for el in arr:

            for exclude in pairs[el]:

                if exclude in arr:
                    return False
        return True

    ingradients = set(range(1, n + 1))
    ans = 0
    for k in range(0, n + 1):

        for combination in itertools.combinations(ingradients, k):
            if not is_possible(combination):
                continue
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
