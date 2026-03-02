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

Solution adapted from: https://github.com/mpfeifer1/Kattis/blob/master/grass.cpp
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
        i = 0
        while i < len(lines):
            n, l, w = list(map(int, lines[i].split()))
            i += 1

            # A list of sprinklers:
            # each is represented by two integers:
            # - left fully watered part
            # - right fully watered part
            sprinklers: list[tuple[float, float]] = []
            for _ in range(n):
                x, r = list(map(int, lines[i].split()))
                i += 1

                # Ignore sprinklers that can't even water one column
                if r <= w / 2:
                    continue

                h = math.sqrt(r**2 - (w / 2.0) ** 2)
                sprinklers.append((max(x - h, 0), min(x + h, l)))

            # Sort all sprinklers along the left fully watered part
            sprinklers = sorted(sprinklers, key=lambda sprinkler: sprinkler[0])

            if self.debug:
                print(sprinklers)

            actual = []
            actual.append(sprinklers[0])
            for sprinkler in sprinklers[1:]:
                if sprinkler[1] > actual[-1][1]:
                    actual.append(sprinkler)
            sprinklers = actual

            target = 0.0
            next = 0.0
            answer = 1
            works = True
            j = 0
            while j < len(sprinklers):

                if sprinklers[j][0] <= target:
                    next = max(next, sprinklers[j][1])
                    j += 1
                    continue

                if abs(target - next) < 0.00001:
                    works = False
                    break

                answer += 1
                target = next

            if next < l:
                works = False

            if works:
                self.put_int(answer)
            else:
                self.put_int(-1)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
