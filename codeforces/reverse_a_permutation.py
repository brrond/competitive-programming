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
            n = int(self.get_string())
            permutation = list(map(int, self.get_string().split()))

            possible_max = n
            left = None
            right = None
            for i, el in enumerate(permutation):
                if left is None:
                    if el != n:
                        left = i
                    else:
                        n -= 1
                else:
                    if el == n:
                        right = i
                        break

            if left is not None:
                permutation[left : right + 1] = reversed(permutation[left : right + 1])

            print(" ".join(map(str, permutation)))


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
