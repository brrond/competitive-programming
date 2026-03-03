"""
Link: https://open.kattis.com/problems/terraces
"""

import sys

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


def main() -> None:
    """Solution goes here."""

    # Inputs
    m, n = get_ints()
    grid = []
    for _ in range(n):
        grid.append(get_ints())

    # BFS
    passt = [[None for _ in range(m)] for _ in range(n)]  # (aka suits)
    processing = [[False for _ in range(m)] for _ in range(n)]

    def is_ok(i: int, j: int) -> bool:
        # Mem
        if passt[i][j] is not None:
            return passt[i][j]

        # Check if any of the neighbors is smaller.
        current = grid[i][j]
        if any(
            [
                i - 1 >= 0 and grid[i - 1][j] < current,
                i + 1 < n and grid[i + 1][j] < current,
                j - 1 >= 0 and grid[i][j - 1] < current,
                j + 1 < m and grid[i][j + 1] < current,
            ]
        ):
            passt[i][j] = False
            return False

        # Check if all the neighbors are taller.
        if all(
            [
                i - 1 < 0 or grid[i - 1][j] > current,
                i + 1 >= n or grid[i + 1][j] > current,
                j - 1 < 0 or grid[i][j - 1] > current,
                j + 1 >= m or grid[i][j + 1] > current,
            ]
        ):
            passt[i][j] = True
            return True

        # Check if all the neighbors are being processed.
        if all(
            [
                i - 1 < 0 or processing[i - 1][j],
                i + 1 >= n or processing[i + 1][j],
                j - 1 < 0 or processing[i][j - 1],
                j + 1 >= m or processing[i][j + 1],
            ]
        ):
            passt[i][j] = True
            return True

        # :(
        # BFS over all neighbors with the same height.
        processing[i][j] = True
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        ok = None
        # from O(1) up to O(n * m)
        for neighbor in neighbors:
            ni, nj = neighbor
            if n > ni >= 0 and m > nj >= 0:
                if grid[ni][nj] == current and not processing[ni][nj]:
                    if ok is None:
                        ok = is_ok(ni, nj)
                    else:
                        ok = ok and is_ok(ni, nj)
                elif grid[ni][nj] > current:
                    if ok is None:
                        ok = True
                    else:
                        ok = ok and True
        processing[i][j] = False

        # O(1)
        if not ok:
            for neighbor in neighbors:
                ni, nj = neighbor
                if n > ni >= 0 and m > nj >= 0 and grid[ni][nj] == current:
                    passt[ni][nj] = False

        passt[i][j] = ok
        return ok

    # O(n * m)
    # and yeah, is_ok can run up to O(n * m),
    # but the overall complexity is still O(n * m),
    # because is_ok will run O(n * m) only once.
    # So it actually something like T(2 * n * m),
    # which is ok.
    for i in range(n):
        for j in range(m):

            if passt[i][j] is None:
                passt[i][j] = is_ok(i, j)

    if DEBUG:
        print(*passt, sep="\n")

    ans = 0
    for i in range(n):
        for j in range(m):
            if passt[i][j]:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
