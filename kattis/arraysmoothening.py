"""
Link: https://open.kattis.com/problems/arraysmoothening
"""

import sys
from collections import defaultdict
import heapq


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

        string = str(string)  # just to make sure
        if self.debug and self.output_file is not None:
            self.output_file.write(string + "\n")
        else:
            sys.stdout.write(string + "\n")

    def solve(self) -> None:
        """Solution goes here."""

        n, k = self.get_ints()
        arr = self.get_ints()
        # frequencies
        frequencies: dict[int, int] = defaultdict(lambda: 0)

        # O(n)
        for el in arr:
            frequencies[el] += 1

        # Edge case 1: there are no elements to remove
        if k == 0:
            self.put_string(str(max(frequencies.values())))
            return

        counts = [CustomInteger(i) for i in list(frequencies.values())]
        heapq.heapify(counts)

        while k != 0:
            heapq.heappush(counts, CustomInteger(heapq.heappop(counts).i - 1))
            k -= 1
        self.put_string(str(counts[0].i))


class CustomInteger:
    def __init__(self, i: int):
        self.i = i

    def __lt__(self, other):
        return self.i > other.i


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
