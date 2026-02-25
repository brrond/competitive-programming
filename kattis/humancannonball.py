"""
Link: https://open.kattis.com/problems/humancannonball

Samples:
0.0 0.0
5.0 5.0
0

Should output:
sqrt(2)

25.0 100.0
190.0 57.5
4
125.0 67.5
75.0 125.0
45.0 72.5
185.0 102.5

Should output:
19.984901
"""

import sys
from functools import cache
from math import sqrt

SPEED = 5.0


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

    def get_floats(self) -> list[float]:
        """Returns floats from the input."""

        return list(map(float, self.get_string().split()))

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

    def put_float(self, f: float, precision: int = 2):
        """Prints the float into the output with the given precision."""

        self.put_string(str(round(f, precision)))

    @cache
    @staticmethod
    def calc_travel_time(a: tuple[float, float], b: tuple[float, float]) -> float:
        x1, y1 = a
        x2, y2 = b
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d / SPEED

    @cache
    @staticmethod
    def calc_flight_time(cannon: tuple[float, float], b: tuple[float, float]) -> float:
        x1, y1 = cannon
        x2, y2 = b
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return abs(d - 50) / SPEED + 2.0

    def solve(self) -> None:
        """Solution goes here."""

        start = to_tuple(self.get_floats())
        finish = to_tuple(self.get_floats())
        n = self.get_int()

        cannons: list[tuple[float, float]] = []
        cannons.append(start)  # same as by finish (see below)
        for i in range(n):
            cannon = to_tuple(self.get_floats())
            cannons.append(cannon)
        cannons.append(finish)

        d = [float("inf") for _ in range(n + 2)]
        d[0] = 0
        d[-1] = CPSolver.calc_travel_time(start, finish)

        # Bellman-Ford
        # Total number of vertices here is n + 2
        # BF works with V - 1
        for _ in range(n + 1):

            # relax all edges
            for i in range(n + 2):
                for j in range(n + 2):

                    if i == j:
                        continue

                    alternative1 = CPSolver.calc_travel_time(cannons[i], cannons[j])
                    alternative2 = (
                        CPSolver.calc_flight_time(cannons[i], cannons[j])
                        if i != 0
                        else float("inf")
                    )

                    cost = min(alternative1, alternative2)
                    d[j] = min(d[j], d[i] + cost)

        self.put_float(d[-1], 10)


def to_tuple(point: list[float]) -> tuple[float, float]:
    return (point[0], point[1])


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
