"""
Link: https://open.kattis.com/problems/goodmorning
"""

import sys
from typing import Callable, Any
from functools import cache

sys.setrecursionlimit(20_000_000)


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

        possible_moves = {
            # First row
            1: [2, 4],
            2: [3, 5],
            3: [6],
            # Second row
            4: [5, 7],
            5: [6, 8],
            6: [9],
            # Third row
            7: [8],
            8: [9, 0],
            9: [],
            # 4th row
            0: [],
        }

        t = self.get_int()
        for _ in range(t):

            inp = self.get_string()
            n = len(inp)
            inp_int = int(inp)

            @cache
            def solve(curr_digit: int, position_in_the_input: int, acc: str) -> str:
                """Returns the best solution for current arguments."""

                if position_in_the_input == n:
                    return acc

                if curr_digit == inp[position_in_the_input]:
                    return solve(
                        curr_digit, position_in_the_input + 1, acc + str(curr_digit)
                    )

                # From this point on there are three options:
                # - don't move and choose current digit one more time
                # - move right
                # - move down

                sol1 = solve(
                    curr_digit, position_in_the_input + 1, acc + str(curr_digit)
                )
                diff1 = abs(inp_int - int(sol1))

                for next_digit in possible_moves[curr_digit]:
                    sol = solve(next_digit, position_in_the_input, acc)
                    diff = abs(inp_int - int(sol))

                    if diff1 > diff:
                        diff1 = diff
                        sol1 = sol

                return sol1

            print(solve(1, 0, ""))


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
