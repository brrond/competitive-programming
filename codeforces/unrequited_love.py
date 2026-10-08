"""
Link:
"""

import sys
from typing import Callable, Any

from collections import defaultdict


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

    def _get_item(self, map_function: Callable[[str], Any]) -> Any:
        return map_function(self.get_string())

    def _get_items(self, map_function: Callable[[str], Any]) -> list[Any]:
        return list(map(map_function, self.get_string().split()))

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return self._get_items(int)

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return self._get_item(int)

    def get_floats(self) -> list[float]:
        """Returns floats from the input."""

        return self._get_items(float)

    def get_float(self) -> float:
        """Returns a float from the input."""

        return self._get_item(float)

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

    def put_ints(self, integers: list[int]) -> None:
        """Prints ints into the output."""

        self.put_string(" ".join(map(str, integers)))

    def put_float(self, f: float, precision: int = 2) -> None:
        """Prints the float into the output."""

        self.put_string(str(round(f, precision)))

    def put_floats(self, floats: list[float], precision: int = 2) -> None:
        """Prints floats into the output."""

        self.put_string(" ".join(map(str, [round(f, precision) for f in floats])))

    def solve(self) -> None:
        """Solution goes here."""

        t = self.get_int()
        while t != 0:
            t -= 1

            n = self.get_int()
            a = self.get_ints()

            # Assumption: Forget about overlapping parts.
            # The task is then very simple: calculate the maximal possible count of pairs,
            # where sums of triads are equal.
            # Basically: find all x, y, where x != y (and y > x, as the order doesn't matter).
            # Naive approach would be:
            # 1. Calculate "loves" for each triad.
            # 2. Iterate all triads.
            # 3. If triad in set -> ans++
            # 4. If not -> add it to set
            #
            # Overlapping parts are only relevant for +2 and +4 indices (the pair must not be added).

            ans = 0
            sums: list[int] = [0] * n
            seen_sums: dict[int, int] = defaultdict(int)
            for i in range(n - 4): # O(n)
                s = a[i] + a[i + 2] - a[i + 4]
                to_ans = seen_sums[s] = seen_sums[s] + 1  # O(log n)
                ans += to_ans - 1

                sums[i] = s # O(1)

                if i >= 2 and sums[i - 2] == s:  # O(1)
                    ans -= 1
                if i >= 4 and sums[i - 4] == s:  # O(1)
                    ans -= 1

            self.put_int(ans)



def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
