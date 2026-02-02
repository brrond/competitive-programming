"""
My Python template for competitive programming.
Includes some basic wrapper logic easy debugging.
"""


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

        n = int(self.get_string())
        prev = self.get_string()

        decs = True
        incr = True
        for _ in range(n - 1):
            curr = self.get_string()

            incr = incr and curr > prev
            decs = decs and prev > curr
            prev = curr

        if incr == decs and not decs:
            print("NEITHER")
        elif incr:
            print("INCREASING")
        elif decs:
            print("DECREASING")


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
