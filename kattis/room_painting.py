"""
My Python template for competitive programming.
Includes some basic wrapper logic easy debugging.
"""

import bisect


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
        return input()

    def solve(self):
        """Solution goes here."""

        n, m = self.get_string().split()
        n = int(n)
        m = int(m)
        cans_set = set()
        for _ in range(n):
            cans_set.add(int(self.get_string()))

        cans = list(sorted(cans_set))

        res = 0
        for _ in range(m):
            needs = int(self.get_string())

            idx = bisect.bisect_left(cans, needs)
            has = cans[idx]

            res += has - needs

        print(res)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
