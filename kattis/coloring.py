"""
Link:
"""

import sys

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

    n = get_int()
    connections: dict[int, list[int]] = {}
    for i in range(n):
        connections[i] = get_ints()

    def backtrack(colors: dict[int, int]) -> int:
        if len(colors) == n:
            return max(colors.values())

        possible_colors = set(range(n))
        i_to_paint = len(colors)
        for el in connections[i_to_paint]:
            possible_colors.discard(colors.get(el, -1))

        best = n
        for possible_color in possible_colors:
            colors[i_to_paint] = possible_color
            best = min(best, backtrack(colors))
            del colors[i_to_paint]

        return best

    print(backtrack({}) + 1)


if __name__ == "__main__":
    main()
