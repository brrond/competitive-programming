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

        t = int(self.get_string())
        for _ in range(t):
            n, s, x = list(map(int, self.get_string().split()))
            arr = list(map(int, self.get_string().split()))
            sum_of_the_arr = sum(arr)

            until_happy = s - sum_of_the_arr
            if until_happy >= 0 and until_happy % x == 0:
                print("YES")
            else:
                print("NO")


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
