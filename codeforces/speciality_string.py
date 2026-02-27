"""
Link: https://codeforces.com/contest/2200/problem/C
"""

import sys


class CPSolver:
    """Class to handle input for debugging."""

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.input_file = None
        self.output_file = None

    def __call__(self):
        """Caller method for the class."""

        if self.debug:
            self.input_file = open("../input.txt", "r", encoding="utf-8")
            self.output_file = open("../output.txt", "w", encoding="utf-8")

        self.solve()

        if self.debug:
            if self.input_file is not None:
                self.input_file.close()
            if self.output_file is not None:
                self.output_file.close()

    def get_string(self) -> str:
        """Get the string either from input file or from user input."""

        if self.debug and self.input_file is not None:
            line = self.input_file.readline()
        else:
            line = sys.stdin.readline()
        return line.strip()

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return list(map(int, self.get_string().split()))

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return int(self.get_string())

    def put_string(self, string: str) -> None:
        """Prints the string into the output."""

        string = str(string)  # just to make sure
        if self.debug and self.output_file is not None:
            self.output_file.write(string + "\n")
        else:
            sys.stdout.write(string + "\n")

    def put_int(self, integer: int) -> None:
        """Prints the int into the output."""

        self.put_string(str(integer))

    def solve(self) -> None:
        """Solution goes here."""

        t = self.get_int()

        for _ in range(t):

            n = self.get_int()
            string = self.get_string()

            if n % 2 == 1:
                self.put_string("NO")
                continue

            while len(string) != 0:
                removed = False
                prev = string[0]
                for i in range(1, len(string)):
                    el = string[i]

                    if el == prev:
                        # can remove this pair
                        string = string[: i - 1] + string[i + 1 :]
                        removed = True
                        break

                    prev = el

                if not removed:
                    break

            if not removed:
                self.put_string("NO")
            else:
                self.put_string("YES")


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
