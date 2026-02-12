"""
Link: https://open.kattis.com/problems/crosscountry
"""

import sys
import math


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

    def solve(self) -> None:
        """Solution goes here."""

        n = self.get_int()
        _2n = math.sqrt(n)
        _4n = math.sqrt(_2n)
        _16n = math.sqrt(_4n)

        possible_i = 1
        for i in range(math.floor(_16n), math.ceil(_4n)):
            if n % i == 0:
                possible_i = i

        if possible_i == 1:
            print(1)
        else:

            for i in range(possible_i, 1, -1):
                if n % (i**9) == 0:
                    print(i)
                    sys.exit(0)

            print(1)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
