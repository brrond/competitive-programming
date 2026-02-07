"""
Link: https://open.kattis.com/problems/crosscountry
"""

import sys
import heapq


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
        return sys.stdin.readline()

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return list(map(int, self.get_string().split()))

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return int(self.get_string())

    def solve(self):
        """Solution goes here."""

        n, s, t = self.get_ints()
        d = []
        for _ in range(n):
            d.append(self.get_ints())

        pq = []  # priority queue (min-heap)
        # add "initial" state
        for j, value in enumerate(d[s]):

            # skip self
            if value == 0:
                continue

            heapq.heappush(pq, (value, j))

        while len(pq) != 0:

            value, i = heapq.heappop(pq)
            if value > d[s][i]:
                continue

            for j, value in enumerate(d[i]):

                # skip self
                if value == 0:
                    continue

                alternative = d[s][i] + value
                if alternative < d[s][j]:
                    d[s][j] = alternative
                    heapq.heappush(pq, (alternative, j))

        print(d[s][t])


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
