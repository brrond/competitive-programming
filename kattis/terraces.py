"""
Link: https://open.kattis.com/problems/terraces
"""

import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(20_000)

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


class UnionFind:
    def __init__(self, n, m):
        self.parents: dict[tuple[int, int], tuple[int, int]] = {}
        self.possible: dict[tuple[int, int], bool] = {}

        for i in range(n):
            for j in range(m):
                self.parents[(i, j)] = (i, j)
                self.possible[(i, j)] = True

    def get_parent(self, key: tuple[int, int]) -> tuple[int, int]:
        curr = key
        while self.parents[curr] != curr:
            curr = self.parents[curr]
        return curr

    def get_possible(self, key: tuple[int, int]) -> bool:
        parent = self.get_parent(key)
        return self.possible[parent]

    def set_possible(self, key: tuple[int, int], value: bool) -> None:
        parent = self.get_parent(key)
        self.possible[parent] = value

    def update_parent(self, key: tuple[int, int], parent: tuple[int, int]) -> None:
        self.parents[key] = parent


def main() -> None:
    """Solution goes here."""

    # Inputs
    m, n = get_ints()
    grid = []
    for _ in range(n):
        grid.append(get_ints())

    # Union Find
    uf = UnionFind(n, m)
    RIGHT_DIRECTION = (0, 1)
    DOWN_DIRECTION = (1, 0)
    neighbor_directions = [(-1, 0), DOWN_DIRECTION, (0, -1), RIGHT_DIRECTION]
    for i in range(n):
        for j in range(m):

            key = (i, j)
            for direction in neighbor_directions:
                ni = i + direction[0]
                nj = j + direction[1]

                if n > ni >= 0 and m > nj >= 0:

                    if grid[i][j] > grid[ni][nj]:
                        uf.set_possible(key, False)

                    if (
                        direction in (RIGHT_DIRECTION, DOWN_DIRECTION)
                        and grid[i][j] == grid[ni][nj]
                    ):
                        uf.update_parent((ni, nj), key)

    if DEBUG:
        for i in range(n):
            for j in range(m):
                print(uf.get_possible((i, j)), end="")
            print()

    ans = 0
    for i in range(n):
        for j in range(m):
            if uf.get_possible((i, j)):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
