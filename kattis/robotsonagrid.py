"""
Link: https://open.kattis.com/problems/goodmorning
"""

import sys
from typing import Callable, Any
from collections import deque


class CPSolver:
    """Class to handle input for debugging."""

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.input_file = None
        self.output_file = None

    def __call__(self):
        """Caller method for the class."""

        if self.debug:
            self.input_file = open("../input.txt", "r", encoding="utf-8")
            self.output_file = open("../output.txt", "w", encoding="utf-8")

        self.solve()

        if self.debug:
            if self.input_file is not None:
                self.input_file.close()
            if self.output_file is not None:
                self.output_file.close()

    def get_string(self) -> str:
        """Get the string either from input file or from user input."""

        if self.debug and self.input_file is not None:
            line = self.input_file.readline()
        else:
            line = sys.stdin.readline()
        return line.strip()

    def _get_item(self, map_function: Callable[[str], Any]) -> Any:
        return map_function(self.get_string())

    def _get_items(self, map_function: Callable[[str], Any]) -> list[Any]:
        return list(map(map_function, self.get_string().split()))

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return self._get_items(int)

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return self._get_item(int)

    def get_floats(self) -> list[float]:
        """Returns floats from the input."""

        return self._get_items(float)

    def get_float(self) -> float:
        """Returns a float from the input."""

        return self._get_item(float)

    def put_string(self, string: str) -> None:
        """Prints the string into the output."""

        string = str(string)  # just to make sure
        if self.debug and self.output_file is not None:
            self.output_file.write(string + "\n")
        else:
            sys.stdout.write(string + "\n")

    def put_int(self, integer: int) -> None:
        """Prints the int into the output."""

        self.put_string(str(integer))

    def put_ints(self, integers: list[int]) -> None:
        """Prints ints into the output."""

        self.put_string(" ".join(map(str, integers)))

    def put_float(self, f: float, precision: int = 2) -> None:
        """Prints the float into the output."""

        self.put_string(str(round(f, precision)))

    def put_floats(self, floats: list[float], precision: int = 2) -> None:
        """Prints floats into the output."""

        self.put_string(" ".join(map(str, [round(f, precision) for f in floats])))

    def solve(self) -> None:
        """Solution goes here."""

        RIGHT = (0, 1)
        DOWN = (1, 0)
        LEFT = (0, -1)
        UP = (-1, 0)

        n = self.get_int()
        grid = []
        for _ in range(n):
            grid.append(self.get_string())

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):

                if i == 0 and j == 0:
                    dp[0][0] = 1
                    continue

                if grid[i][j] == "#":
                    continue

                paths_to_get_here = 0
                for d in [LEFT, UP]:
                    ni = i + d[0]
                    nj = j + d[1]

                    if n > ni >= 0 and n > nj >= 0:
                        paths_to_get_here += dp[ni][nj]

                dp[i][j] = paths_to_get_here

        if self.debug:
            print(*dp, sep="\n")

        paths = dp[n - 1][n - 1]
        if paths != 0:
            print(paths % (2**31 - 1))
            return

        # BFS
        q: deque[tuple[int, int]] = deque()
        q.append((0, 0))
        visited = [[False for _ in range(n)] for _ in range(n)]
        possible = False

        while len(q) != 0:

            i, j = q.popleft()
            if i == n - 1 and j == n - 1:
                possible = True
                break

            if visited[i][j]:
                continue
            visited[i][j] = True

            for d in [RIGHT, DOWN, LEFT, UP]:
                ni = i + d[0]
                nj = j + d[1]

                if (
                    n > ni >= 0
                    and n > nj >= 0
                    and not visited[ni][nj]
                    and grid[ni][nj] != "#"
                ):
                    q.append((ni, nj))

        if possible:
            print("THE GAME IS A LIE")
        else:
            print("INCONCEIVABLE")


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
