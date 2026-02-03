"""
Link: https://open.kattis.com/problems/bridgesandtunnels
"""


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

    def solve(self):
        """Solution goes here."""

        # O(1)
        n = int(self.get_string())
        parent = {}
        size = {}

        # Best: O(1)
        # Worst: O(n), but after that O(1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # O(1)
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return size[ra]

            # Union by size
            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]
            return size[ra]

        for _ in range(n):
            building1, building2 = self.get_string().split()

            if building1 not in parent:
                parent[building1] = building1
                size[building1] = 1

            if building2 not in parent:
                parent[building2] = building2
                size[building2] = 1

            result = union(building1, building2)
            print(result)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
