"""
Link: https://codeforces.com/contest/2277/problem/C

Extra tests:
2
3 1
1 3
2 3
2
3 1
1 3
2 3
3
"""

import sys
from collections import deque
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

        t = self.get_int()
        while t != 0:
            t -= 1

            # Read input
            n, m = self.get_ints()
            connections: list[list[int]] = [[] for _ in range(n)]
            for _ in range(n - 1):  # O(n)
                x, y = self.get_ints()

                a = x - 1
                b = y - 1
                connections[a].append(b)
                connections[b].append(a)
            operations = self.get_ints()  # O(m)

            # Do I have to calculate path in order to determine
            # if the new order is better than current?
            # - no
            # lets say:
            #
            # depth(x, y) - length of the path from x to y
            # d = depth(1, n)
            # l = depth(1, v), where v is v_i from operation
            # j = depth(1, w), where w is joint point of path (1, n) and (1, v)
            #
            # Let's say, the new path is better. It means:
            # d_new > d => d_new - d > 0
            #
            # d_new = (d - j) + (l - j) + 1 (- d from both parts)
            # d_new - d = d - j + l - j + 1 - d
            # d_new - d = - j + l - j + 1 =>
            # - j + l - j + 1 > 0
            # l - 2j + 1 > 0 (and l - 2j + 1 gives the increment to the answer)
            #
            # Assumptions:
            # 1. I only look at the subtree from the root in which destination node is located.
            # 2. There are basically two operations:
            #    1. Delete newly created edge (aka do nothing)
            #    2. Delete one of the edges in path (1, w)
            # 3. Deleted edge (x) from path (1, w) must always be
            #    the first edge after the root (1, x).
            #    This way the other edges on path (e, x) can be reused.

            # One important thing (Hint): It suffices to use one operation this way and
            # delete the newly added edge in all others. Nothing better is possible:
            # every added edge is incident to 1, so a simple path from 1 to n in the final tree
            # uses at most one of them, as its first edge, and then follows an original path
            # from vi to n avoiding 1

            # Determine the depth of the path from each vertex to n.
            # BFS
            depths: list[int] = [-1 for _ in range(n)]
            visited: list[bool] = [False for _ in range(n)]
            nodes: deque[tuple[int, int]] = deque()
            nodes.append((0, n - 1))
            while len(nodes) != 0:
                depth, node = nodes.popleft()
                depths[node] = depth
                visited[node] = True

                # Skip other path over 0.
                if node == 0:
                    continue

                for el in connections[node]:
                    if visited[el]:
                        continue

                    nodes.append((depth + 1, el))

            ans = depths[0]
            for el in operations:  # O(m)
                v = el - 1

                if v in [0, n - 1]:
                    continue

                ans = max(ans, depths[v] + 1)

            self.put_int(ans)


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
