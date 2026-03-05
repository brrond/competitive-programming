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
    can_have_simmilar_color: dict[int, set[int]] = {}
    for i in range(n):
        connections[i] = get_ints()
        can_have_simmilar_color[i] = set(range(n))
        can_have_simmilar_color[i].discard(i)
        for el in connections[i]:
            can_have_simmilar_color[i].discard(el)

    if DEBUG:
        for key, similar in can_have_simmilar_color.items():
            print(f"{key}: {similar}")

    not_colored = list(range(n))
    ans = 0
    while len(not_colored) != 0:

        i = not_colored[0]
        for el in can_have_simmilar_color[i]:
            if el in not_colored:
                not_colored.remove(el)
        not_colored.remove(i)
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
