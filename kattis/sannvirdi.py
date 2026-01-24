"""
Link: https://open.kattis.com/problems/sannvirdi

Dröfn Karen loves the new game show, Sannvirði, in the television programme schedule.
What she enjoys the most is seeing how happy the winner is once they receive the prize.
She is thrilled to watch each episode.

Each episode begins with the game show host displaying some item you may find for sale,
for example, a refrigerator, an automobile, a carrot, a bottle of perfume, and so forth.
All the contestants get to view the item for the same amount of time.
Then the contestants must guess what the real value of the item is.
The contestant which guesses closest, but not above, the correct answer is the winner.
Contestants make their guesses simultaneously and cannot see the guesses of other contestants.
However, the viewers, such as Dröfn, receive all of the information.
The show cuts to very short interviews with each contestant where they explain their guess.

Of course, we cannot have television content without commercials.
Before the winner is announced, the show cuts to a commercial break.
Dröfn is shaking in excitement.
She has her own ideas of the item’s real value and wonders
what contestant would win if any of her ideas were the correct answer.

Can you find the winner for each of Dröfn’s ideas?
Input

The first line consists of one integer, the number of contestants.

Next,
lines follow, each describing a contestant.
A contestant’s description consists of a name and a guess, separated by a space.
Each name consists of at least and at most English lowercase characters.
Each guess is an integer between and

, inclusive on both ends. You may assume that no two contestants guessed the same value.

A line containing one integer

, the number of ideas, follows.

Finally,
lines follow, each describing one of Dröfn’s ideas. Each idea is an integer between and

, inclusive on both ends.
Output

For each idea, in the same order they appear in the input, output the name of the contestant
which wins if that idea were the correct answer.
If no contestant wins for the idea, you should output :(, since Dröfn will be sad if nobody wins.
Scoring

Group


Points


Constraints

1


10


,

2


15


,

3


20


,

4


25


,

5


30


,
Sample Input 1 	Sample Output 1

1
Hannes 10
1
9



:(

Sample Input 2 	Sample Output 2

3
Eva 500
Sammi 100
Arnar 1000
4
1000000000
500
499
250



Arnar
Eva
Sammi
Sammi
"""

DEBUG = True
FILE = None


def get_string() -> str:
    """Get the string either from input file or from user input."""
    if DEBUG and FILE is not None:
        return FILE.readline()
    return input()


def find_right(arr: list[int], n: int) -> int:
    """
    e : arr[:e] <= n, arr[e:] > n
    """

    l = 0
    r = len(arr) - 1
    while l < r:
        m: int = (l + r) // 2

        if arr[m] > n:
            r = m
        elif arr[m] < n:
            l = m + 1
        else:
            return m
    return r


def main():
    """Main method."""

    n = int(get_string())
    guess2name = dict()
    for _ in range(n):
        name, guess_str = get_string().split()
        guess2name[int(guess_str)] = name
    guesses = sorted(list(guess2name.keys()))

    q = int(get_string())
    for _ in range(q):
        idea = int(get_string())
        idx = find_right(guesses, idea)
        guess = guesses[idx]

        if guess <= idea:
            print(guess2name[guess])
        elif guess > idea and idx != 0:
            print(guess2name[guesses[idx - 1]])
        else:
            print(":(")


if __name__ == "__main__":
    if DEBUG:
        FILE = open("../input.txt", "r", encoding="utf-8")
    main()
    if DEBUG and FILE is not None:
        FILE.close()
