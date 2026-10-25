"""
Link:
"""

from __future__ import annotations
import sys
from collections import deque, defaultdict
from typing import Callable, Any, Optional
from dataclasses import dataclass


@dataclass
class Node:
    id: int
    parent: Optional[Node]
    children: list[Node]
    childer_ids: set[int]


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
            nodes: list[Node] = [Node(i, None, [], set()) for i in range(n)]  # O(n)
            root: Node = nodes[0]
            for _ in range(n - 1):  # O(n)
                x, y = self.get_ints()

                parent = nodes[x - 1]
                child = nodes[y - 1]

                parent.children.append(child)
                parent.childer_ids.add(y - 1)
                child.parent = parent
            operations = self.get_ints()  # O(m)

            # Original calculations.
            depths: dict[int, int] = self.calculate_depths(root)  # O(n)
            path: list[Node] = self.calculate_path(nodes)  # O(n)
            ans = len(path)

            for el in operations:  # O(m)
                v = el - 1

                if v in root.childer_ids or v == 0 or v == n - 1:  # O(1)
                    continue

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

                # Determine junction point (w) and j (depth(w))
                w = self.calculate_junction_point(nodes[v], [node.id for node in path])
                if w.id == root.id:
                    continue
                j = depths[w.id]

                # Determine l
                l = depths[v]

                # New path is batter than old
                gain = l - 2 * j + 1
                if gain > 0:
                    ans += gain

            self.put_int(ans)

    def calculate_depths(self, root: Node) -> dict[int, int]:
        """
        Calculates depths for all nodes in the list.
        Returns a dict, where:
        keys - ids of nodes
        values - depths of nodes

        Complexity: O(n).
        """

        depths: dict[int, int] = defaultdict(int)  # depth[x] = y => depth(1, x) = y
        nodes2try: list[Node] = [root]
        while len(nodes2try) != 0:

            curr = nodes2try.pop(0)
            for child in curr.children:
                nodes2try.append(child)

            if curr.parent is not None:
                depths[curr.id] = depths[curr.parent.id] + 1
        return depths

    def calculate_path(self, nodes: list[Node]) -> list[Node]:
        """
        Calculates the path from n up to 0.

        Complexity: O(n).
        """

        path: deque[Node] = deque()
        curr: Optional[Node] = nodes[-1]
        while curr is not None:
            path.appendleft(curr)
            curr = curr.parent
        return path

    def calculate_junction_point(self, curr: Node, path_ids: list[int]) -> Node:
        """
        Determines junction point from curr to path given by path_ids.

        Complexity: O(n).
        """

        while curr.parent is not None:
            if curr.id in path_ids:
                break
            curr = curr.parent
        return curr


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
