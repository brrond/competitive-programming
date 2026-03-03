"""
Link: https://open.kattis.com/problems/largesthoarding

9
1 1
2 1
3 1
4 1
5 1
4 1
3 1
2 1
1 1

    *
   ***
  88888
 *88888*
**88888**
750

11
3 1
3 1
0 1
1 6
0 1
2 1
2 1
2 1
0 1
2 2
3 1

**              *
**        *** ***
** ****** *** ***
300
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

    def solve(self) -> None:
        """Solution goes here."""

        n = self.get_int()

        # Calculate clusters.
        # A cluster consists of buildings.
        # Each building is represented by w and h.
        clusters: list[list[tuple[int, int]]] = []
        curr_cluster: list[tuple[int, int]] = []

        # List of all possible heights.
        # The resulting hoarding will have one of these heights.
        # Worst case - 100 different heights
        possible_heights: set[int] = set()

        for _ in range(n):
            h, w = self.get_ints()

            if h == 0 and len(curr_cluster) != 0:
                # new cluster
                clusters.append(curr_cluster)

                curr_cluster = []
                continue

            curr_cluster.append((w, h))
            possible_heights.add(h)

        # Add last cluster
        if len(curr_cluster) != 0:
            clusters.append(curr_cluster)
        # End of cluster calculation

        # O(100 * log 100)
        possible_heights_list = sorted(list(possible_heights))

        # Try to find maximal possible area for each cluster.
        # O(k), where k is the number of clusters.
        largest_area = 0
        for cluster in clusters:

            # Iterate all possible heights (worst case - 100).
            for height in possible_heights_list:

                area = 0

                # Iterate all buildings in cluster.
                # O(n) along ALL clusters.
                for building in cluster:
                    w, h = building

                    if h >= height:
                        # Current building can contribute to total area.
                        area += w * height
                    else:
                        # Current building is too small for current height.
                        largest_area = max(largest_area, area)
                        area = 0

                largest_area = max(largest_area, area)

        print(largest_area * 50)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
