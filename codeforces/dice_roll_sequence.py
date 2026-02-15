"""
Link: https://codeforces.com/contest/2195/problem/C
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

            n = self.get_int()
            arr = self.get_ints()

            res = 0
            ignore = False
            for i in range(n - 1):

                curr = arr[i]
                next = arr[i + 1]

                if ignore:
                    ignore = False
                elif next in (curr, 7 - curr):
                    res += 1
                    ignore = True

            print(res)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
