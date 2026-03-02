"""
Link:
"""

import sys
import heapq
import math

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


def calc_distance(nodes, i, j) -> float:
    x1, y1 = nodes[i]
    x2, y2 = nodes[j]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def add_edges(visited, pq, nodes, node):
    visited[node] = True

    for i in range(len(nodes)):
        if visited[i]:
            continue

        heapq.heappush(pq, (calc_distance(nodes, node, i), node, i))


def main():
    n = get_int()
    for _ in range(n):

        m = get_int()
        islands = []
        for _ in range(m):
            x, y = get_floats()
            islands.append((x, y))

        # Prim's algo
        mst_cost = 0.0
        mst_node_count = 1
        visited = [False] * m

        pq = []
        add_edges(visited, pq, islands, 0)
        while len(pq) != 0 and mst_node_count < m:

            cost, _, end = heapq.heappop(pq)

            if visited[end]:
                continue

            add_edges(visited, pq, islands, end)
            mst_node_count += 1
            mst_cost += cost

        print(mst_cost)


if __name__ == "__main__":
    main()
