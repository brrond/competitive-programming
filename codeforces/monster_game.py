"""
Link: https://codeforces.com/contest/2193/problem/D
"""

import bisect


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

    def get_n_of_available_swords(self, a, x) -> int:
        return len(a) - bisect.bisect_left(a, x)

    def get_score(self, sum_b, available_swords: int) -> int:
        return bisect.bisect_right(sum_b, available_swords)

    def solve(self):
        """Solution goes here."""

        t = int(self.get_string())
        for _ in range(t):
            n = int(self.get_string())
            a = list(map(int, self.get_string().split()))
            b = list(map(int, self.get_string().split()))

            sum_b = []
            curr = 0
            for el in b:
                curr += el
                sum_b.append(curr)

            # The question is to find the best score.
            # For that an optimal x must be found.
            # Search region for x is [min(sword), max(sword))
            swords = sorted(a)

            # O(n)
            best_score = 0
            for el in swords:
                # O(log n)
                available_swords = self.get_n_of_available_swords(swords, el)

                # O(log n)
                score = self.get_score(sum_b, available_swords) * el

                best_score = max(score, best_score)

            print(best_score)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
