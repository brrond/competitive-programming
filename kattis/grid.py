"""
Link:
"""

import sys
from typing import Callable, Any


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

        mem: dict[tuple[int, int], int] = {}
        mem[(n - 1, m - 1)] = 0

        # A set of indices that are currently being processed
        processing: set[tuple[int, int]] = set()

        def calc(i: int, j: int) -> int:
            """
            Returns the minimal number of step to go from (i, j)
            to the end of the grid (n, m).
            """

            key = (i, j)
            if key in mem.keys():
                return mem[key]

            if key in processing:
                return -2

            best = None

            # Calculate possible jump directions
            k = grid[i][j]

            # There are no moves to make
            if k == 0:
                mem[key] = -1
                return -1

            processing.add(key)

            possible_directions = []
            if j + k < m:
                possible_directions.append("RIGHT")
            if i + k < n:
                possible_directions.append("DOWN")
            if i - k >= 0:
                possible_directions.append("UP")
            if j - k >= 0:
                possible_directions.append("LEFT")

            # Try all possible jump directions
            for direction in possible_directions:

                new_i = i
                new_j = j
                if direction == "UP":
                    new_i -= k
                elif direction == "DOWN":
                    new_i += k
                elif direction == "LEFT":
                    new_j -= k
                else:
                    new_j += k

                alternative = calc(new_i, new_j)
                if alternative == -2:
                    # Current key is still being processed.
                    # Skip
                    continue

                if alternative == -1:
                    # Current branch has no solutions
                    # Skip
                    continue

                if best is None:
                    best = alternative
                best = min(alternative, best)

            processing.remove(key)

            if best is None:
                mem[key] = -1
                return -1
            # else:
            mem[key] = best + 1
            return best + 1

        self.put_int(calc(0, 0))


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
