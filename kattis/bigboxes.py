"""
Link: https://open.kattis.com/problems/bigboxes?tab=metadata
"""

import sys
from functools import cache

sys.setrecursionlimit(200_000)

DEBUG = True

if DEBUG:
    with open("../input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    lines = sys.stdin.readlines()

n, k = list(map(int, lines[0].split()))
weights = list(map(int, lines[1].split()))

# calc sum array
sums = []
last_sum = 0
for el in weights:
    last_sum += el
    sums.append(last_sum)


@cache
def get_sum(l, r):
    """
    Returns the sum on [l, r] interval (inclusive both ends).

    Complexity: O(1).
    """

    return sums[r] - sums[l] + weights[l]


@cache
def solve(l=0, r=n - 1, current_k=k) -> int:
    """
    Returns optimal solution for the problem:
    Minimum possible maximal sum of the elements in one group.

    l, r - left and right position in array,
    current_k - current number of boxes to put items into.

    Complexity: O(k*n!)
    """

    # impossible
    if l > r:
        return 0

    # there can be one sum only
    if current_k == 1:
        return get_sum(l, r)

    # "bite" first part of the array
    # on split_position location.
    # After that, current_k - 1 boxes are possible
    best_max_sum = None

    # [l, r)
    for split_position in range(l, r + 1):

        # calc sum of the current box
        curr_sum = get_sum(l, split_position)

        # calculate the alternative solution
        alternative = solve(split_position + 1, r, current_k - 1)

        # calculate potential best solution in this case
        potential_best = max(alternative, curr_sum)

        if best_max_sum is None or potential_best < best_max_sum:
            best_max_sum = potential_best

    return best_max_sum


print(solve())
