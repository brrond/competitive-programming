"""
Link: https://open.kattis.com/problems/commercials
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

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return list(map(int, self.get_string().split()))

    def solve(self):
        """Solution goes here."""

        _, p = self.get_ints()
        breaks = [el - p for el in self.get_ints()]

        best = 0
        curr_sum = 0
        for cost in breaks:
            curr_sum = max(cost, curr_sum + cost)
            best = max(best, curr_sum)
        print(best)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
