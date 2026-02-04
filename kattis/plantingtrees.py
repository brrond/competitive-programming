"""
Link: https://open.kattis.com/problems/plantingtrees
"""

import sys

DEBUG = True

if DEBUG:
    with open("../input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    lines = sys.stdin.readlines()
n = int(lines[0])
trees = list(map(int, lines[1].split()))

# the assumption is,
# trees that require more time
# should be planted first.
sorted_trees = sorted(trees, reverse=True)

# with this assumption it's only necessary
# to calculate the latest day when the last plant
# grows.
current_latest = 1
for i, el in enumerate(sorted_trees):
    # day starts with 1
    possible_latest = (i + 1) + el
    current_latest = max(current_latest, possible_latest)

# More precisely, the party can be organized
# at earliest on the next day after the last tree has grown up.
print(current_latest + 1)
