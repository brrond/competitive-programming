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

            # Total love for each triad from each index
            # are gonna be considered.
            # O(n)
            triads = defaultdict(list)
            for i in range(n):
                position = i

                next_position = position + 2
                if next_position < n:

                    next_next_position = next_position + 2
                    if next_next_position < n:

                        s = a[position] + a[next_position] - a[next_next_position]
                        triads[s].append(i)

            # print(pairs)
            # defaultdict(<class 'list'>, {7: [0, 1]})
            # defaultdict(<class 'list'>, {0: [0, 1, 2]})
            # defaultdict(<class 'list'>, {0: [0, 1, 2, 7], -6: [3], -5: [4, 6], 2: [5]})
            # Not all "loves" are possible here.

            # In the second case (0, 1, 2), possible pairs are:
            # 0 1 and 1 2, but not 0 2
            # So the answer is 2.

            # In the third case, possible pairs are:
            # 0 1, 1 2, 2 7, 0 7, 1 7
            # So the answer is 5.

            # Sums with no pairs are not checked.
            # Each sum is checked separately and won't overlap with other sums.
            # Each pair in one sum won't overlap, if:
            # - diff of indices > 4 OR
            # - diff of indices % 2 != 0
            # So each triad of numbers, which give the same sum, must be checked for the total number of pairs.
            # Naiv algorithm gives something like O(n^3):
            # for each sum: (1)
            #     for each element (el1) which gives sum: (2)
            #         for each next element (el2) which gives sum: (3)
            #             if index suits el1 el2:
            #                 ans++
            # But in reality O(n^3) is not achievable.
            # If (1) is O(n) then (2) and (3) are O(1) => O(n)
            # If (2) is O(n) then (3) is also O(n) (but actually optimized, as in bubble sort),
            # but (1) is O(1) => O(n^2)
            # From problem statement:
            # sum of n over all testcases <= 2 * 10^5.

            ans = 0
            for _, pairs in triads.items():

                for i, el1 in enumerate(pairs):
                    for el2 in pairs[i + 1:]:
                        diff = el2 - el1
                        if diff > 4 or diff % 2 != 0:
                            ans += 1

            self.put_int(ans)





def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
