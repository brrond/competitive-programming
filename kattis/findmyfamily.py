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
    heights_with_index = [(height, i) for i, height in enumerate(h)]

    # O(n log n)
    sorted_heights = sorted(
        heights_with_index,
        key=lambda height_with_index: height_with_index[0],
    )

    if DEBUG:
        print(sorted_heights)

    # O(n)
    for i, (my_height, my_index) in enumerate(sorted_heights):

        alice_height = None
        # O(n)
        for sorted_alice_index, (
            possible_alice_height,
            possible_alice_index,
        ) in enumerate(sorted_heights[i + 1 :]):

            if possible_alice_height > my_height and possible_alice_index < my_index:
                alice_height = possible_alice_height
                break

        bob_height = None
        if alice_height is not None:

            # O(n)
            for possible_bob_height, possible_bob_index in sorted_heights[
                sorted_alice_index + 1 :
            ]:

                if possible_bob_height > alice_height and possible_bob_index > my_index:
                    bob_height = possible_bob_height
                    break

        if bob_height is not None:
            res.append(photo_index + 1)
            break


print(len(res))
print(*res, sep="\n")

# O(n^2)
