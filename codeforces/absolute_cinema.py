"""
Link: https://codeforces.com/contest/2195/problem/D
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
            return self.input_file.readline()
        return sys.stdin.readline()

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return list(map(int, self.get_string().split()))

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return int(self.get_string())

    def put_string(self, string: str) -> None:
        """Prints the string into the output."""

        if self.debug and self.output_file is not None:
            self.output_file.write(string + "\n")
        else:
            sys.stdout.write(string + "\n")

    def solve(self):
        """Solution goes here."""

        t = self.get_int()
        for _ in range(t):

            n = self.get_int()
            fi = self.get_ints()

            arr = [0] * n
            total_sum = 0
            total_sum_for_last = 0

            for index in range(2, n):
                i = index - 1

                ai = (fi[i + 1] - 2 * fi[i] + fi[i - 1]) // 2
                arr[i] = ai
                total_sum += ai
                total_sum_for_last += i * ai

            a_last = (fi[0] - total_sum_for_last) / (n - 1)
            arr[n - 1] = a_last
            total_sum += a_last

            arr[0] = fi[1] - fi[0] + total_sum

            arr = map(int, arr)
            self.put_string(" ".join(map(str, arr)))


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
