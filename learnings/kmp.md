# Knuth-Morris-Pratt (KMP)

Algorithm for pattern finding in string.
Complexity: O(n)

Consist of two parts:
1. Creation of Longest Prefix Suffix (LPS)
2. Usage of LPS to find the pattern

## LPS

First step is to find LPS. The idea of this array is that there can probably be multiple prefixes in pattern and we have to find all of them to be able to "move" the pattern minimum amount of cells to continue the search efficiently.

Minimal example:
```python
def get_lps(p: str) -> list[int]:
    """
    Calculates the longest prefix suffix of pattern p.

    Input:  sususu
    Output: 001234

    Input:  ababcab
    Output: 0012012

    Input:  ababaab
    Output: 0012312
    """

    lps = [0]
    j = 0  # iterator over "pattern"
    i = 1  # current position in the lps

    while i < len(p):

        if p[i] == p[j]:
            j += 1
            i += 1
            lps.append(j)
        else:
            if j == 0:
                i += 1
                lps.append(0)
            else:
                j = lps[j - 1]

    return lps
```

## KMP

The idea now is to apply lps to the string similarly as "prefix". 
- If char matches -> continue
- If reached the end of the pattern -> found match + start from the most largest previous prefix
- If not match:
  - If not in "prefix" (j == 0) -> continue
  - If is in "prefix" (j != 0) -> got to the previous longest prefix

```python
def kmp(s: str, p: str) -> list[int]:
    """
    Return the positions of all occurrences
    of the pattern p in string s.
    """

    lps = get_lps(p)

    i = 0  # position in string
    j = 0  # position in lps/pattern

    positions: list[int] = []

    while i < len(s):

        if s[i] == p[j]:
            i += 1
            j += 1

            if j == len(p):
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return positions


```

## Problems

kattis/String Matching
