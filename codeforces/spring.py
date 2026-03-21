"""
Link:
"""

import sys
from typing import Callable, Any

import heapq


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

    def gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self.gcd(b % a, a)

    def lcd(self, a: int, b: int) -> int:
        return (a * b) // self.gcd(a, b)

    def solve(self) -> None:
        """Solution goes here."""

        t = self.get_int()
        for _ in range(t):

            a, b, c, m = self.get_ints()

            n_a = m // a
            n_b = m // b
            n_c = m // c

            ab = self.lcd(a, b)
            bc = self.lcd(b, c)
            ac = self.lcd(a, c)
            abc = self.lcd(ab, self.lcd(bc, ac))

            n_abc = m // abc

            n_ab = m // ab - n_abc
            n_ac = m // ac - n_abc
            n_bc = m // bc - n_abc

            n_a = n_a - n_ab - n_ac - n_abc
            n_b = n_b - n_ab - n_bc - n_abc
            n_c = n_c - n_ac - n_bc - n_abc

            ans_a = n_a * 6 + n_ab * 3 + n_ac * 3 + n_abc * 2
            ans_b = n_b * 6 + n_ab * 3 + n_bc * 3 + n_abc * 2
            ans_c = n_c * 6 + n_ac * 3 + n_bc * 3 + n_abc * 2

            print(ans_a, ans_b, ans_c)


def main():
    """Main method."""

    CPSolver(False)()


if __name__ == "__main__":
    main()
