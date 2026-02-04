"""
Link: https://open.kattis.com/problems/walrusweights
"""

import sys
import bisect

DEBUG = True

if DEBUG:
    with open("../input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    lines = sys.stdin.readlines()

n = int(lines[0])

# sorted weights
weights = sorted(list(map(int, lines[1:])))

if DEBUG:
    print(weights)


# The question is: what is the closest to 1000 sum
# of the elements in the array.

# Assume the best sum is x.
# Search area: x in [min(weights), sum(weights)]
# The problem here is, it's possible that
# 1000 not in [min(weights), sum(weights)]
# There are two edge cases:
# 1. 1000 < min(weights) (!impossible by problem statement)
# 2. 1000 > sum(weights)

sum_of_weights = sum(weights)

# Edge case 1000 > sum(weights)
if sum_of_weights <= 1000:
    print(sum_of_weights)

else:

    def find_best_to_curr(x, sub_weights) -> int:
        """
        O(log sub_weights)
        """

        return bisect.bisect_left(sub_weights, x)

    curr_best = 0
    i = 0

    # O(n)
    for el in reversed(weights):
        curr = el

        if abs(1000 - curr) < abs(1000 - curr_best):
            curr_best = curr

        sub_weights = weights[: -i - 1]
        while len(sub_weights) != 0:  # O(n)

            i_to_append = find_best_to_curr(abs(1000 - curr), sub_weights)
            if i_to_append >= len(sub_weights):
                i_to_append -= 1

            curr += sub_weights.pop(i_to_append)
            if abs(1000 - curr) > abs(1000 - curr_best):
                break
            else:
                curr_best = curr

        i += 1

    print(curr_best)

# Worst case: O(n^2)
# But optimized: O(n log n)
# as each iteration over n smaller portion of elements is taken:
# n, n - 1, n - 2, etc and on each of them binary search is performed.
