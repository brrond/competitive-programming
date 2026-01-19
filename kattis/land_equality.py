"""
https://open.kattis.com/problems/landequality

There is a kingdom where the old King wants to divide his land into two pieces
and give them to his two descendants. The King’s land is a grid of rows and columns.
Each cell in the grid has an integer value representing the prosperity of the cell,
which can be (deserted), (regular), or

(fertile). Two cells are connected if they share a side horizontally or vertically.

Each descendant shall receive a single connected piece of land with at least one cell,
in which all cells must be directly connected or indirectly connected via other cells.
There shall be no leftover cells, which means that each cell must be given to one descendant.
The prosperity of a piece of land is the product of all the prosperity values of its cells.
The King wants the absolute difference between the prosperity of the two descendants’ land to be
as small as possible. He has asked his best counselor to devise a land division plan
between the two descendants.

Input

The first line of input contains two positive integers r and c (2 <= r * c <= 64).
The next lines each have integers giving the prosperity values of the King’s land.
All those integers are 0, 1, or 2.

Output

Output the smallest absolute difference between the prosperity of the two descendants’ land.
Sample Input 1 	Sample Output 1

3 4
1 2 1 1
2 2 1 2
1 2 2 2

8

Sample Input 2 	Sample Output 2

2 3
0 1 2
0 1 2

0

Sample Input 3 	Sample Output 3

1 3
2 0 2

2

Learnings:
- counting dict or smth
"""

import copy


def parse_input():
    """Parses the user input."""

    r, _ = map(int, str(input()).split())
    elements = {0: 0, 1: 0, 2: 0}
    grid = []
    for _ in range(r):
        row = list(map(int, str(input()).split()))

        grid.append(row)

        for el in row:
            elements[el] += 1

    return elements, grid


def main():
    """Main function."""

    elements, grid = parse_input()

    if elements[0] != 0:  # there are zeros

        if elements[0] >= 2:  # if there are at least two zeros
            print(0)

        else:  # elements[0] == 1

            if elements[1] != 0:
                print(1)
            else:
                print(2)

    else:

        if elements[2] == 0:  # there are only 1s

            print(0)

        else:  # the result dependents on 2s

            print(int(find_solution(grid, elements)))


def find_solution(grid: list[list[int]], elements: dict[int, int]) -> int:
    """
    Divide the grid into two parts:
    A and B
    """

    return dfs(grid, 1, 2 ** elements[2], [], (0, 0))


def dfs(
    grid: list[list[int]],
    a_prosperity: int,
    b_prosperity: int,
    A: list[tuple[int, int]],
    curr: tuple[int, int],
) -> int:
    curr_el = grid[curr[0]][curr[1]]
    a_prosperity *= curr_el
    b_prosperity /= grid[curr[0]][curr[1]]
    A.append(curr)

    connected = calc_connected(grid, A, curr)
    best_score = abs(b_prosperity - a_prosperity)
    for connection in connected:
        best_score = min(
            best_score,
            dfs(grid, a_prosperity, b_prosperity, copy.deepcopy(A), connection),
        )

    return best_score


def calc_connected(
    grid: list[list[int]], A: list[tuple[int, int]], curr: tuple[int, int]
) -> list[tuple[int, int]]:
    """Calc connected nodes."""

    connected = []

    i, j = curr
    if (i + 1) < len(grid):
        connected.append((i + 1, j))
    if (j + 1) < len(grid[0]):
        connected.append((i, j + 1))
    if (i - 1) >= 0:
        connected.append((i - 1, j))
    if (j - 1) >= 0:
        connected.append((i, j - 1))

    res = []
    for connection in connected:
        if connection not in A:
            res.append(connection)

    return res


if __name__ == "__main__":
    main()
