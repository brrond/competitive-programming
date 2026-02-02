"""
Link: https://open.kattis.com/problems/rot

Damir likes to rotate. Right now he is rotating tables of letters.
He wrote an R x C table onto a piece of paper.
He has also chosen an angle K, a multiple of 45,
and wants to rotate his table that many degrees clockwise.

It turns out this task is a bit too hard for Damir, so help him out.

Input

The first line contains two integers R and C separated
by a space (1 <= R, C <= 10), the number of rows and columns in Damir’s table.
Each of the next R lines contains one row of Damir’s table, a string of lowercase letters.
The last line contains an integer K, a multiple of 45 between 0 and 360 (inclusive).

Output

Output Damir’s table rotated K degrees clockwise, like shown in the examples.
The output should contain the smallest number of rows necessary.
Some rows may have leading spaces, but no rows may have trailing spaces.

Sample Input 1 	Sample Output 1

3 5
damir
marko
darko
45



  d
 m a
d a m
 a r i
  r k r
   k o
    o

My examples:
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


def rotate(table: list[str], k: int, n: int, m: int) -> list[str]:
    if k == 0 or k == 360:
        return table, None

    quadrats = k // 90
    quadrats_reminder = k % 90
    subquadrat = quadrats_reminder // 45

    if quadrats == 0:
        rotated_quadrats = table
    elif quadrats == 1:
        # 90 deg
        # each column becomes a row with reversed order
        rotated_quadrats = []
        for j in range(m):
            tmp = ""
            for i in range(n - 1, -1, -1):
                tmp += table[i][j]
            rotated_quadrats.append(tmp)

    elif quadrats == 2:
        # 180 deg
        # each row and each column is reversed
        rotated_quadrats = ["".join(reversed(s)) for s in list(reversed(table))]

    elif quadrats == 3:
        # 270 deg
        # each column becomes a row
        # the order order of rows is reversed
        rotated_quadrats = []
        for j in range(m - 1, -1, -1):
            tmp = ""
            for i in range(n):
                tmp += table[i][j]
            rotated_quadrats.append(tmp)

    # recalculate n, m
    n, m = len(rotated_quadrats), len(rotated_quadrats[0])

    # at this point there is either 45 rotation
    # or no rotation at all

    if subquadrat == 0:
        # no extra rotation -> done
        return rotated_quadrats, None

    # rotate 45 deg
    # number of rows in 45 deg rotated matrix is n + m - 1
    # let us say, we have following example
    # 2 2 2 2
    # 2 2 2 2
    # 2 2 2 2
    # 2 2 2 2
    #
    #    2
    #   2 2  (1)
    #  2 2 2
    # 2 2 2 2
    #  2 2 2
    #   2 2  (2)
    #    2
    # number of diagonal elements along side (1) is width
    # the total number of rows consist of extra elements
    # along side (2). The question is, how many such rows exist?
    # Actually height rows.
    # Because the element on position (3) is calculated twice
    # subtract -1.
    size = n + m - 1
    rotated_subquadrats: list[list[str]] = [[" "] * size for _ in range(size)]

    # write row by row
    row_offset = 0
    column_offset = m - 1
    for row in rotated_quadrats:
        for i, el in enumerate(row):
            rotated_subquadrats[row_offset + i][column_offset + i] = el

        row_offset += 1
        column_offset -= 1

    return ["".join(row) for row in rotated_subquadrats]


# Read input
r, c = list(map(int, input().split()))
table: list[str] = []
for _ in range(r):
    s = input()
    table.append(s)
k = int(input())

# Rotate the matrix clockwise
rotated_table = rotate(table, k, r, c)

# Print matrix
for row in rotated_table:
    print(row)
