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

            n, q = list(map(int, self.get_string().split()))
            a = list(map(int, self.get_string().split()))
            b = list(map(int, self.get_string().split()))

            a_reversed = list(reversed(a))
            b_reversed = list(reversed(b))
            curr_max = a_reversed[0]
            curr_sum = 0
            for i, el in enumerate(a_reversed):
                curr_max = max([el, curr_max, b_reversed[i]])
                curr_sum += curr_max
                a_reversed[i] = curr_sum
            a_reversed.insert(0, 0)

            answers = []
            for _ in range(q):
                l, r = list(map(int, self.get_string().split()))
                l -= 1
                r -= 1
                r, l = n - l - 1, n - r - 1
                answers.append(a_reversed[r + 1] - a_reversed[l])
            print(" ".join(map(str, answers)))


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
