"""
Link: https://open.kattis.com/problems/grandpabernie
"""

n = int(input())
countries = dict()
for _ in range(n):
    country, year_str = input().split()
    year = int(year_str)

    if country not in countries:
        countries[country] = []

    countries[country].append(year)

countries2work = dict()
for key, years in countries.items():
    countries2work[key] = sorted(years)

q = int(input())
output = []
for _ in range(q):
    country, i_str = input().split()
    i = int(i_str)

    output.append(countries2work[country][i - 1])

print(*output, sep="\n")
