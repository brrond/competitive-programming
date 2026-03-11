"""
Link: https://codeforces.com/contest/2194/problem/C
"""

import sys


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

        t = self.get_int()
        for _ in range(t):

            n, k = self.get_ints()

            # read input and save each char of each line
            # as possible char for corresponding position.
            lines = []
            possible_chars_for_each_position = [set() for _ in range(n)]
            for _ in range(k):
                line = self.get_string().strip()
                lines.append(line)

                for i, el in enumerate(line):
                    possible_chars_for_each_position[i].add(el)

            # determine d
            d = 1
            while d <= n:

                if n % d != 0:
                    continue

                possible = True
                possible_chars = []

                for group_element_index in range(d):

                    possible_chars_for_group = possible_chars_for_each_position[
                        group_element_index
                    ].copy()

                    for group_start_index in range(group_element_index, n, d):

                        possible_chars_for_group = (
                            possible_chars_for_group.intersection(
                                possible_chars_for_each_position[group_start_index]
                            )
                        )

                    if len(possible_chars_for_group) == 0:
                        possible = False
                        break

                    possible_chars.append(possible_chars_for_group)

                if possible:
                    prefix = "".join([min(set_) for set_ in possible_chars])
                    times = n // d + 1
                    print((prefix * times)[:n])
                    break

                d += 1


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
