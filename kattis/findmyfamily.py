"""
Link: https://open.kattis.com/problems/findmyfamily
"""

import sys

DEBUG = True

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
    max_right = [0] * n
    max_right[-1] = h[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], h[i])

    if DEBUG:
        print(max_right)

    stack = []  # Potential Alice's height
    stack.append(h[0])
    i = 1
    while i < n:  # O(n)

        height = h[i]
        if height < stack[-1]:
            while len(stack) != 0 and stack[-1] > height:  # O(n) BUT
                # in reality O(k) where k is number of i's where h[i] > h[i - 1]
                last_poped = stack.pop(-1)

            if max_right[i] > last_poped > height:
                res.append(photo_index + 1)
                break

        stack.append(h[i])
        i += 1

print(len(res))
print(*res, sep="\n")
