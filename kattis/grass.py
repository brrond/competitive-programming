"""
Link: https://open.kattis.com/problems/grass

Sample input:
8 20 2
5 3
4 1
1 2
7 2
10 2
13 3
16 2
19 4
3 10 1
3 5
9 3
6 1
3 10 1
5 3
1 1
9 1

Sample output:
6
2
-1
"""

import sys
from typing import Callable, Any, Optional

import math


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

    def get_all_strings(self) -> list[str]:
        """Gets all strings from the input."""

        if self.debug and self.input_file is not None:
            lines = self.input_file.readlines()
        else:
            lines = sys.stdin.readlines()
        return [line.strip() for line in lines]

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

        lines = self.get_all_strings()
        lines.pop(-1)
        while len(lines) != 0:
            n, l, w = list(map(int, lines.pop(0).split()))

            # A list of sprinklers:
            # each is represented by two integers:
            # - the distance from left side to the left part of rectangle
            # that is being watered
            # - x position
            # - radius
            sprinklers: list[tuple[float, int, int]] = []
            for _ in range(n):
                x, r = list(map(int, lines.pop(0).split()))

                # Ignore sprinklers that can't even water one column
                if r < w:
                    continue

                h = math.sqrt(r**2 - (w / 2) ** 2)
                sprinklers.append((x - h, x, r))

            # Sort all sprinklers along first argument
            sprinklers = sorted(sprinklers, key=lambda sprinkler: sprinkler[0])

            if self.debug:
                print(sprinklers)

            strip_to_be_watered = 0.0
            sprinkler_i = 1
            sprinkler_to_use: Optional[tuple[float, int, int]] = sprinklers[0]
            abort = False
            answer = 0
            while strip_to_be_watered < l:

                # Can try to find better sprinkler
                if sprinkler_i < len(sprinklers):
                    sprinkler = sprinklers[sprinkler_i]

                    # Find the best next sprinkler
                    if sprinkler[0] <= strip_to_be_watered:
                        sprinkler_to_use = sprinkler
                        sprinkler_i += 1
                        continue

                if sprinkler_to_use is None:
                    abort = True
                    break

                # The best sprinkler to use is found
                a, x, r = sprinkler_to_use
                if a > strip_to_be_watered:
                    abort = True
                    break

                answer += 1
                h = x - a
                strip_to_be_watered = x + h
                sprinkler_to_use = None

            if abort:
                self.put_int(-1)
            else:
                self.put_int(answer)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
