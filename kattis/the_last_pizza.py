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
        slices = [int(self.get_string()) for _ in range(n)]

        if n == 1:
            if slices[0] & 1 == 0:
                print("Ja")
            else:
                print("Nej")
        elif n == 2:
            if slices[0] & 1 == 0 and slices[1] & 1 == 0:
                print("Nej")
            else:
                # (slices[0] % 1 == 1 and slices[1] % 1 == 1) or
                # (either of slices % 1 == 0 another % 1 != 0)
                print("Ja")
        else:
            even = 0
            ones = 0

            for el in slices:
                if el & 1 == 0:
                    even += 1
                elif el == 1:
                    ones += 1

            if even in [2, 3]:
                print("Ja")
            elif even == 2:
                if ones == 0:
                    print("Nej")
                else:
                    print("Ja")
            else:
                print("Nej")


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
