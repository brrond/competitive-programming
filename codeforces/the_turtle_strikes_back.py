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

            best = find_best_variant(matrix, n, m)

            max_pleasure_i = 0
            for i, el in enumerate(best.pleasures):
                if el > best.pleasures[max_pleasure_i]:
                    max_pleasure_i = i

            pos = best.path[max_pleasure_i]
            matrix[pos[0]][pos[1]] *= -1

            print(find_best_variant(matrix, n, m).total)


class Variant:
    def __init__(self, path: list[tuple[int, int]], pleasures: list[int], total: int):
        self.pleasures = pleasures
        self.path = path
        self.total = total

    def __repr__(self) -> str:
        return f"{self.path} {self.pleasures} ({self.total})"

    def __lt__(self, other):
        return self.total > other.total


def find_best_variant(matrix: list[list[int]], n: int, m: int) -> Variant:
    full_paths: list[Variant] = []
    variants = [Variant([(0, 0)], [matrix[0][0]], matrix[0][0])]
    while len(variants) != 0:

        variant = variants.pop(0)
        i, j = variant.path[-1]
        if i == n - 1 and j == m - 1:
            heapq.heappush(full_paths, variant)
            continue

        if i < n - 1:
            clone = copy.deepcopy(variant)
            clone.path.append((i + 1, j))
            clone.pleasures.append(matrix[i + 1][j])
            clone.total += matrix[i + 1][j]
            variants.append(clone)

        if j < m - 1:
            clone = copy.deepcopy(variant)
            clone.path.append((i, j + 1))
            clone.pleasures.append(matrix[i][j + 1])
            clone.total += matrix[i][j + 1]
            variants.append(clone)
    return full_paths[0]


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
