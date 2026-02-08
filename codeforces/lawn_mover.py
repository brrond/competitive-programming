"""
Link: https://codeforces.com/contest/2194/problem/A
"""

import sys


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

        t = self.get_int()
        for _ in range(t):

            n, w = self.get_ints()
            if w == 1:
                print(0)
            else:
                print(n // w * (w - 1) + n % w)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
