"""
Link:
"""

import sys

DEBUG = True

input_file = None
if DEBUG:
    input_file = open("../input.txt", "r", encoding="utf-8")


def get_string() -> str:
    """Returns a string from the input."""

    if DEBUG and input_file is not None:
        line = input_file.readline()
    else:
        line = sys.stdin.readline()
    return line.strip()


def get_int() -> int:
    """Returns an integer from the input."""

    return int(get_string())


def get_ints() -> list[int]:
    """Returns integers from the input."""

    return list(map(int, get_string().split()))


def get_float() -> float:
    """Returns a float from the input."""

    return float(get_string())


def get_floats() -> list[float]:
    """Returns floats from the input."""

    return list(map(float, get_string().split()))


class UnionFind:
    def __init__(self, friends: list[str]):
        n = len(friends)
        self.n = n
        self.parents = {}
        self.counts = {}
        for friend in friends:
            self.parents[friend] = friend
            self.counts[friend] = 1

    def find(self, f: str) -> str:
        curr = f
        while curr != self.parents[curr]:
            curr = self.parents[curr]
        self.parents[f] = curr
        return curr

    def union(self, f1: str, f2: str) -> None:
        p1 = self.find(f1)
        p2 = self.find(f2)

        self.parents[p2] = p1
        self.counts[p1] += self.counts[p2]

    def find_count(self, f: str) -> int:
        return self.counts[self.find(f)]


def main() -> None:
    """Solution goes here."""

    t = get_int()
    for _ in range(t):

        f = get_int()
        people = set()
        connections: list[tuple[str, str]] = []
        for _ in range(f):
            name1, name2 = get_string().split()
            people.add(name1)
            people.add(name2)
            connections.append((name1, name2))

        outs = ""
        uf = UnionFind(list(people))
        for connection in connections:
            f1, f2 = connection
            uf.union(f1, f2)
            outs += str(uf.find_count(f2)) + "\n"
        print(outs)


if __name__ == "__main__":
    main()
