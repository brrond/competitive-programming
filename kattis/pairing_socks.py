"""
Link: https://open.kattis.com/problems/pairingsocks
"""

from collections import deque


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

        n = int(self.get_string())
        socks = list(map(int, self.get_string().split()))

        # the left part is "top"
        first = deque()
        for sock in socks:
            first.append(sock)
        second = deque()

        res = 0
        second.appendleft(first.popleft())
        res += 1

        while len(first) != 0:

            f = first.popleft()
            s = second.popleft()

            if f == s:
                res += 1

                if len(second) == 0 and len(first) != 0:
                    second.appendleft(first.popleft())
                    res += 1
            else:
                second.appendleft(s)
                second.appendleft(f)
                res += 1

        if len(second) == 0:
            print(res)
        else:
            print("impossible")


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
