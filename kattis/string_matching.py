"""
String Matching

Input
The input consists of several test cases. Each test case consists of two lines, first a non-empty pattern, then a non-empty text. Input is terminated by end-of-file. The input file will not be larger than 5 Mb.

Output
For each test case, output one line containing the positions of all the occurences of pattern in text, from first to last, separated by a single space.
Sample Input 1 	Sample Output 1

p
Popup
helo
Hello there!
peek a boo
you speek a bootiful language
anas
bananananaspaj


2 4

5
7
"""

import sys

for line in sys.stdin:
    p = line[:-1]
    s = sys.stdin.readline()[:-1]

    curr = s
    out = []
    offset = 0
    while p in curr:
        start = curr.find(p)
        out.append(start + offset)
        offset = start + 1

        if start + 1 >= len(curr):
            break
        curr = curr[start + 1 :]

    print(" ".join(map(str, out)))
