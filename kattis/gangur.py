"""
Link: https://open.kattis.com/problems/gangur


Gangur
Languages
en
is
/problems/gangur/file/statement/en/img-0001.jpg
Hallway by Chuttersnap, Unsplash
Several people are walking through a narrow hallway.
When two people meet they have to turn to the side to pass each other.
The hallway is split into sections.
In some sections there is a person and some sections are empty.
Each person is facing either end of the hallway and they all walk at the same speed.
How many people have had to pass each other when all individuals
have walked to their end of the hallway?
Input

The input consists of a single line describing the contents of all the section of the hallway.
The hallway is at least
section and at most

sections. If the hallway is described by > then there is a person there facing right.
If the hallway is described by < then there is a person there facing left.
If the hallway is described by - then there is no person there.
Output

The output should contain a single integer, the number of times two people
pass each other in the hallway.
Scoring

Group


Points


Constraints

1


25


The only section described by > is the first section

2


25


All > are to the left of <

3


25


There are at most

sections

4


25


No further constraints
Sample Input 1 	Sample Output 1

>-<-<<-<



4

Sample Input 2 	Sample Output 2

>->>-->-<<-<<<



20

Sample Input 3 	Sample Output 3

<><-<->-<



4
"""


class CPSolver:
    """Class to handle input for debugging."""

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.file = None

    def __call__(self):
        """Caller method for the class."""

        if self.debug:
            self.file = open("../input.txt", "r", encoding="utf-8")
        self.solve()
        if self.debug and self.file is not None:
            self.file.close()

    def get_string(self) -> str:
        """Get the string either from input file or from user input."""

        if self.debug and self.file is not None:
            return self.file.readline()
        return input()

    def solve(self):
        """Solution goes here."""

        # pidor -> a person moving from left to right
        # mudak -> a person moving from right to left
        pidors = 0
        total = 0
        line = self.get_string()
        for el in line:
            if el == "<":
                total += pidors
            elif el == ">":
                pidors += 1
        print(total)


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
