"""
Link: https://open.kattis.com/problems/orders?editresubmit=19095627
"""

import sys
from functools import cache

sys.setrecursionlimit(200000)

DEBUG = True

if DEBUG:
    with open("../input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    lines = sys.stdin.readlines()

n = int(lines[0])
menu = list(map(int, lines[1].split()))
m = int(lines[2])
orders = list(map(int, lines[3].split()))

# describes the path (taken or not)
solutions: dict[tuple[int, int], bool] = {}


@cache
def solve(t: int, s: int = 0) -> int:
    """
    This function returns part solution for current (t)otal with
    the assumption, that we start with (s)tart element of the menu.
    """

    if t == 0:
        return 1
    if t < 0:
        return 0
    if s == n:
        return 0

    found_one_solution = False
    product = menu[s]
    if product == 0:
        return 0

    # take current product
    r1 = solve(t - product, s)
    if r1 == 2:
        return 2
    if r1 == 1:
        # save that current element must be taken
        solutions[(t, s)] = True
        found_one_solution = True

    # skip current product
    r2 = solve(t, s + 1)
    if r2 == 2:
        return 2
    if r2 == 1:
        # save that current element must not be taken
        solutions[(t, s)] = False
        found_one_solution = True

    if r1 == 1 and r2 == 1:
        return 2

    if found_one_solution:
        return 1
    return 0


for order in orders:
    s = solve(order)

    if s == 0:
        print("Impossible")
    elif s == 2:
        print("Ambiguous")
    else:
        # reconstruct path

        t = order
        s = 0

        solution = []
        while t != 0:

            if solutions[(t, s)]:
                # must take
                t -= menu[s]
                solution.append(s + 1)
            else:
                # must skip
                s += 1
        print(*solution)
