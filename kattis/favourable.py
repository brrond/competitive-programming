"""
Link:
"""

import sys
from collections import defaultdict
from functools import cache

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
        s = get_int()

        graph: dict[int, list[int]] = defaultdict(list)
        for _ in range(s):
            inp = get_string().split()
            a = int(inp[0])
            if len(inp) == 4:
                arr = list(map(int, inp[1:]))

                for el in arr:
                    graph[a].append(el)
            else:
                if inp[1] == "catastrophically":
                    graph[a].append(-1)
                else:
                    graph[a].append(0)

        if DEBUG:
            for key, values in graph.items():
                print(f"{key}: {values}")

        @cache
        def find_n_solutions(start: int) -> int:

            solutions = 0
            for el in graph[start]:
                if el == -1:
                    continue
                if el == 0:
                    solutions += 1
                    continue

                solutions += find_n_solutions(el)

            return solutions

        print(find_n_solutions(1))


if __name__ == "__main__":
    main()
