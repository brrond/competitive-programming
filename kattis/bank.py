"""
Link: https://open.kattis.com/problems/bank
"""

import sys

DEBUG = True

if DEBUG:
    with open("../input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    lines = sys.stdin.readlines()

n, t = list(map(int, lines[0].split()))

customers: list[tuple[int, int]] = []
for i in range(n):
    c, t_i = list(map(int, lines[i + 1].split()))

    customers.append((c, t_i))

# O(n log n)
customers = sorted(customers, key=lambda c: c[0], reverse=True)

if DEBUG:
    print(customers)


# Try to serve a customer with more cash at the last possible moment
# or earlier
used_times: list[bool] = [False] * t
number_of_available_time_windows = t
total = 0
for customer in customers:
    cash, leave_time = customer

    # find the latest available time window
    while used_times[leave_time] and leave_time >= 0:
        leave_time -= 1

    # customer can't be served
    if leave_time < 0:
        continue

    used_times[leave_time] = True
    total += cash
    number_of_available_time_windows += 1

    if number_of_available_time_windows == t:
        break

print(total)
