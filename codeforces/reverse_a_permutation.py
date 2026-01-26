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

            max_index = None
            for i in range(0, len(permutation) - 1):
                for j in range(i + 1, len(permutation)):

                    if permutation[j] > permutation[i]:

                        if max_index is None:
                            max_index = j
                        elif permutation[j] > permutation[max_index]:
                            max_index = j

                if max_index is not None:
                    break

            if max_index is not None:
                permutation[i : max_index + 1] = reversed(
                    permutation[i : max_index + 1]
                )

            print(" ".join(map(str, permutation)))


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
