"""
Link: https://open.kattis.com/problems/findmyfamily
"""

import sys
import bisect

DEBUG = False

if DEBUG:
    f = open("../input.txt", "r", encoding="utf-8")


def get_line() -> str:
    if DEBUG:
        return f.readline()
    return sys.stdin.readline()


k = int(get_line())
res = []
for photo_index in range(k):

    n = int(get_line())
    h = list(map(int, get_line().split()))

    if DEBUG:
        print(h)

    # O(n)
    max_right = [0] * len(h)
    max_right[-1] = h[-1]
    for i in range(len(h) - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], h[i])

    if DEBUG:
        print(max_right)

    # O(n log n)
    second_min_left = [-1] * len(h)
    sorted_heights = [h[0]]
    # -1 means there are no second min until current point
    for iterable_i, height in enumerate(h[1:]):  # O(n)
        i = iterable_i + 1

        # O(log n)
        insert_index = bisect.bisect_right(sorted_heights, height)
        if insert_index == len(sorted_heights):
            sorted_heights.append(height)
            continue

        # O(log n)
        # Worst case: O(n)
        second_min_left[i] = sorted_heights[insert_index]
        bisect.insort_left(sorted_heights, height)

    if DEBUG:
        print(second_min_left)

    # O(n)
    for i, height in enumerate(h):

        second_min = second_min_left[i]
        if max_right[i] > second_min > height:
            res.append(photo_index + 1)
            break


print(len(res))
print(*res, sep="\n")
