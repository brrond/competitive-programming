"""
Link:
"""

import sys
from copy import deepcopy
from typing import Callable, Any


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

        MAX = 10**6

        t = self.get_int()
        while t != 0:
            t -= 1

            # Read input
            n, m = self.get_ints()
            nodes: list[list[int]] = [[] for _ in range(n)]  # O(n)
            for _ in range(n - 1):  # O(n)
                x, y = self.get_ints()
                nodes[x - 1].append(y - 1)
            operations = self.get_ints()

            # Print initial paths
            path = self.find_path(nodes, 0, n - 1)

            if self.debug:
                print("Original:", path)

            # Check if "greedy" approach helps.
            # To check, if selecting the best solution for each operation,
            # helps improve the final score, I will simply try it.
            # Brute force for now.
            for el in operations:  # O(m)
                v = el - 1

                if v in nodes[0]:
                    continue

                prev_nodes = deepcopy(nodes)  # O(n ^ 2)
                subpath = self.find_path(nodes, 0, v)
                if self.debug:
                    print(subpath)

                nodes[0].remove(subpath[1])
                nodes[0].append(v)
                prev = subpath[1]
                for i in range(2, len(subpath)):  # O(n)
                    curr = subpath[i]
                    nodes[prev].remove(curr)
                    nodes[curr].append(prev)
                    prev = curr

                new_path = self.find_path(nodes, 0, n - 1)
                if len(new_path) > len(path):
                    path = new_path
                else:  # new_path < path:
                    nodes = prev_nodes

            if self.debug:
                print("End:", path)
            self.put_int(len(path) - 1)

    def find_path(self, nodes: list[list[int]], f: int, t: int) -> list[int]:
        """
        DFS for path between nodes from f to t.
        O(n).
        """

        if f == t:
            return [t]

        for node in nodes[f]:
            path = self.find_path(nodes, node, t)
            if len(path) != 0:
                return [f] + path

        return []


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
