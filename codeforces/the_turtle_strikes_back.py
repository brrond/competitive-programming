"""
Link: https://codeforces.com/contest/2194/problem/E
"""

import sys
import copy
import heapq


class CPSolver:
    """Class to handle input for debugging."""

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.file = None

    def __call__(self):
        """Caller method for the class."""

        if self.debug:
            self.file = open("../input.txt", "r", encoding="utf-8")
        self.solve()
        if self.debug and self.file is not None:
            self.file.close()

    def get_string(self) -> str:
        """Get the string either from input file or from user input."""

        if self.debug and self.file is not None:
            return self.file.readline()
        return sys.stdin.readline()

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return list(map(int, self.get_string().split()))

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return int(self.get_string())

    def solve(self):
        """Solution goes here."""

        inf = -(10**10)
        t = self.get_int()
        for _ in range(t):

            n, m = self.get_ints()
            matrix = [self.get_ints() for _ in range(n)]
            cache = dict()

            def calc_best_path(i: int, j: int) -> tuple[list[tuple[int, int]], int]:

                if i + 1 == n and j + 1 == m:
                    return [(i, j)], matrix[i][j]

                key = (i, j)
                if key in cache:
                    return cache[key]

                alt1 = alt2 = None
                if i + 1 < n:
                    alt1 = calc_best_path(i + 1, j)
                if j + 1 < m:
                    alt2 = calc_best_path(i, j + 1)

                if alt1 is None and alt2 is not None:
                    path, t = alt2
                    path.append(key)
                    t += matrix[i][j]
                    alt2 = (path, t)
                    cache[key] = alt2
                    return alt2

                if alt1 is not None and alt2 is None:
                    path, t = alt1
                    path.append(key)
                    t += matrix[i][j]
                    alt1 = (path, t)
                    cache[key] = alt1
                    return alt1

                if alt1 is not None and alt2 is not None:
                    if alt1[1] > alt2[1]:
                        path, t = alt1
                        path.append(key)
                        t += matrix[i][j]
                        alt1 = (path, t)
                        cache[key] = alt1
                        return alt1
                    path, t = alt2
                    path.append(key)
                    t += matrix[i][j]
                    alt2 = (path, t)
                    cache[key] = alt2
                    return alt2

                raise RuntimeError()

            path, _ = calc_best_path(0, 0)

            max_pleasure_i = 0
            for i, pos in enumerate(path):
                el = matrix[pos[0]][pos[1]]
                if el > matrix[path[max_pleasure_i][0]][path[max_pleasure_i][1]]:
                    max_pleasure_i = i

            pos = path[max_pleasure_i]
            matrix[pos[0]][pos[1]] *= -1
            cache.clear()

            _, total = calc_best_path(0, 0)
            print(total)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
