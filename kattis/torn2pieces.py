"""
Link: https://open.kattis.com/problems/torn2pieces
"""

import sys
from collections import defaultdict
from queue import deque

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
    graph: dict[str, set[str]] = defaultdict(set)
    for _ in range(n):

        stations = get_string().split()
        for station in stations[1:]:

            # Add route from this station to current.
            graph[stations[0]].add(station)

            # Add reverse route (all routes are bi-directional).
            graph[station].add(stations[0])
    start, finish = get_string().split()

    # BFS
    # Each dp state describes a path.
    dp: deque[list[str]] = deque()
    dp.append([start])
    result = None

    while len(dp) != 0 and result is None:

        path = dp.popleft()

        # dead end
        if path[-1] not in graph:
            continue

        for station in graph[path[-1]]:

            # Skip loop.
            if station in path:
                continue

            # Create a copy of the path with a new station.
            tmp_path = path[::]
            tmp_path.append(station)
            dp.append(tmp_path)

            # We have a winner!
            if station == finish:
                result = tmp_path
                break

    if result is None:
        print("no route found")
        return

    print(" ".join(result))


if __name__ == "__main__":
    main()
