"""
1 2 3 4
5 6 7 8
8 10 11 12

  1
 5 2
8 6 3
10 7 4
 11 8
  12

1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

  1
 1 1
1 1 1
1 1 1
1 1 1
 1 1
  1


2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2

   2
  2 2
 2 2 2
2 2 2 2
 2 2 2
  2 2
   2


1 2 3
4 5 6
7 8 9
10 11 12

  1
 4 2
7 5 3
10 8 6
 11 9
  12
"""

from typing import Optional


def rotate(table: list[list[int]], k: int) -> tuple[list[list[int]], Optional[int]]:
    if k == 0 or k == 360:
        return table, None

    quadrats = k // 90
    quadrats_reminder = k % 90
    subquadrat = quadrats_reminder // 45

    n, m = len(table), len(table[0])

    if quadrats == 0:
        rotated_quadrats = table
    elif quadrats == 1:
        rotated_quadrats = []

        for j in range(m):
            rotated_quadrats.append([])

            for i in range(n - 1, -1, -1):
                rotated_quadrats[-1].append(table[i][j])

    elif quadrats == 2:
        rotated_quadrats = table[::-1]

        for i in range(n):
            rotated_quadrats[i] = rotated_quadrats[i][::-1]
    elif quadrats == 3:
        rotated_quadrats = []

        for j in range(m - 1, -1, -1):
            rotated_quadrats.append([])

            for i in range(n):
                rotated_quadrats[-1].append(table[i][j])

    if subquadrat == 0:
        return rotated_quadrats, None
    # subquadrat == 1:
    rotated_subquadrats: list[list[int]] = []

    d = 0
    max_len = 0
    while True:

        rotated_subquadrats.append([])
        i = d
        j = 0

        while i >= n:
            i -= 1
            j += 1

        while j < m and i >= 0:
            rotated_subquadrats[-1].append(table[i][j])
            i -= 1
            j += 1

        l = len(rotated_subquadrats[-1])
        if l == 1 and d != 0:
            break

        max_len = max(l, max_len)
        d += 1

    return rotated_subquadrats, max_len


# Read input
r, _ = list(map(int, input().split()))
table = []
for _ in range(r):
    table.append(list(map(int, input().split())))
k = int(input())

# Rotate the matrix clockwise
rotated_table, max_len = rotate(table, k)

if max_len is None:

    for row in rotated_table:
        print(" ".join(map(str, row)))

else:

    for row in rotated_table:
        print(" " * (max_len - len(row)) + " ".join(map(str, row)))
