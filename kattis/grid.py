"""
Link:
"""

import sys
from typing import Callable, Any

from queue import deque


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

        n, m = self.get_ints()
        grid = []

        for _ in range(n):
            s = self.get_string()

            row = []
            for el in s:
                row.append(int(el))
            grid.append(row)

        # BFS
        # For this implementation I use deque, because insertion and deletion O(1)
        # For each path current node is saved as i, j, visited
        # i, j is the position in the grid
        # visited is a set of already visited positions (i, j)-pairs
        # visited set is required because there can be loops
        paths = deque()
        paths.append((0, 0, set()))

        curr_len = 0  # current max depth (answer)
        found = False  # True, if node (n - 1, m - 1) (finish) was reached
        while len(paths) != 0:
            # queue for next possible paths
            new_paths = deque()

            # iterate all reached nodes
            while len(paths) != 0:
                i, j, visited = paths.pop()

                # Finish was reached
                if i == n - 1 and j == m - 1:
                    found = True
                    break

                # Skip loop
                if (i, j) in visited:
                    continue
                k = grid[i][j]
                visited.add((i, j))

                # There are no other nodes
                if k == 0:
                    continue

                # Add all possible variants
                if i - k >= 0:
                    new_paths.append((i - k, j, visited))
                if i + k < n:
                    new_paths.append((i + k, j, visited))
                if j - k >= 0:
                    new_paths.append((i, j - k, visited))
                if j + k < m:
                    new_paths.append((i, j + k, visited))

            if found:
                break

            # New state
            paths = new_paths
            curr_len += 1

        # If the finish was reached, curr_len is the answer
        if found:
            self.put_int(curr_len)
        else:
            self.put_int(-1)

        # Because loops are skipped, worst case is O(nm) if all the elements of the grid are 1


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
