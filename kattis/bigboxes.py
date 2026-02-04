"""
Link: https://open.kattis.com/problems/bigboxes?tab=metadata
"""

import sys

sys.setrecursionlimit(200_000)

DEBUG = True

if DEBUG:
    with open("../input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    lines = sys.stdin.readlines()

n, k = list(map(int, lines[0].split()))
weights = list(map(int, lines[1].split()))

# The question is, what is the minimum possible maximum
# sum of splits.
# It's possible to make an assumption that our solution is x.
# The search region for: x in [max(weights); sum(weights)]
# The question is, is it possible to create such a split,
# that all parts: sum(part) <= x.


def can_split(x):
    """
    O(n)
    """

    current_k = 1
    curr_sum = 0

    for el in weights:
        if curr_sum + el > x:
            current_k += 1
            curr_sum = el
        else:
            curr_sum += el

        if current_k > k:
            break

    return current_k <= k


# Worst case is when max(weights) = 1 and sum(weights) = 100_000
# The complexity of the search is therefore O(log n)
l = max(weights)
r = sum(weights)
while l < r:
    m = (l + r) // 2

    if can_split(m):
        r = m
    else:
        l = m + 1
print(l)

# Final complexity: O(n log n)
