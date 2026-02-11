"""
Link: https://open.kattis.com/problems/crosscountry
"""

import sys
from typing import Optional
from functools import cache


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

    def solve(self) -> None:
        """Solution goes here."""

        NOTHING = 0
        LEFT = -1
        RIGHT = 1

        while True:

            n, k = self.get_ints()
            if n == 0:
                break

            grid: list[list[int]] = []
            total_sum = 0
            for _ in range(n):
                v1, v2 = self.get_ints()
                grid.append([v1, v2])
                total_sum += v1 + v2

            @cache
            def solve(i: int, k_left: int, prev_choice: Optional[int]) -> Optional[int]:
                if k_left < 0:
                    return None

                if i == n and k_left != 0:
                    return None
                if i == n and k_left == 0:
                    return 0

                possible_choices = [NOTHING, LEFT, RIGHT]
                if prev_choice == LEFT:
                    possible_choices.remove(RIGHT)
                if prev_choice == RIGHT:
                    possible_choices.remove(LEFT)

                min_solution = None
                for choice in possible_choices:

                    curr = 0
                    next_k = k_left
                    if choice == LEFT:
                        curr = grid[i][0]
                        next_k -= 1
                    elif choice == RIGHT:
                        curr = grid[i][1]
                        next_k -= 1

                    s = solve(i + 1, next_k, choice)
                    if s is not None:
                        if min_solution is None:
                            min_solution = s + curr
                        else:
                            min_solution = min(s + curr, min_solution)

                return min_solution

            solution = solve(0, k, None)
            assert solution is not None
            print(total_sum - solution)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
