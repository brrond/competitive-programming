"""
Link: https://open.kattis.com/problems/millionairemadness

7 5
10 11 12 13 14
11 20 16 17 16
12 10 18 21 24
14 10 14 14 22
16 18 20 20 25
25 24 22 10 25
26 27 28 21 25

1 4
4 3 2 1

3 3
1 2 3
6 5 4
7 8 9

"""

import sys
import heapq

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

    n, m = get_ints()
    grid = []
    for i in range(n):
        grid.append(get_ints())

    # Dijkstra
    RIGHT = (0, 1)
    DOWN = (1, 0)
    UP = (-1, 0)
    LEFT = (0, -1)
    pq: list[tuple[int, tuple[int, int]]] = [(0, (0, 0))]

    visited = [[False for _ in range(m)] for _ in range(n)]
    while len(pq) != 0:

        cost, key = heapq.heappop(pq)
        i, j = key

        if visited[i][j]:
            continue
        visited[i][j] = True

        if key == (n - 1, m - 1):
            print(cost)
            break

        for d in (RIGHT, DOWN, UP, LEFT):
            ni = i + d[0]
            nj = j + d[1]

            if n > ni >= 0 and m > nj >= 0 and not visited[ni][nj]:

                heapq.heappush(pq, (max(grid[ni][nj] - grid[i][j], 0, cost), (ni, nj)))


if __name__ == "__main__":
    main()
