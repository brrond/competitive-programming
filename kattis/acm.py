"""
Link:
"""

import sys
from collections import defaultdict


class CPSolver:
    """Class to handle input for debugging."""

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.input_file = None
        self.output_file = None

    def __call__(self):
        """Caller method for the class."""

        if self.debug:
            self.input_file = open("../input.txt", "r", encoding="utf-8")
            self.output_file = open("../output.txt", "w", encoding="utf-8")

        self.solve()

        if self.debug:
            if self.input_file is not None:
                self.input_file.close()
            if self.output_file is not None:
                self.output_file.close()

    def get_string(self) -> str:
        """Get the string either from input file or from user input."""

        if self.debug and self.input_file is not None:
            return self.input_file.readline()
        return sys.stdin.readline()

    def get_ints(self) -> list[int]:
        """Returns integers from the input."""

        return list(map(int, self.get_string().split()))

    def get_int(self) -> int:
        """Returns an integer from the input."""

        return int(self.get_string())

    def put_string(self, string: str) -> None:
        """Prints the string into the output."""

        string = str(string)  # just to make sure
        if self.debug and self.output_file is not None:
            self.output_file.write(string + "\n")
        else:
            sys.stdout.write(string + "\n")

    def solve(self) -> None:
        """Solution goes here."""

        solved_problems: set[str] = set()
        penalties: dict[str, int] = defaultdict(lambda: 0)
        final_score = 0
        while True:

            inp = self.get_string().strip()
            if inp == "-1":
                break

            time_str, problem, solved_str = inp.split()
            time = int(time_str)
            solved = "right" == solved_str

            if solved and problem not in solved_problems:
                # First right solution of the problem
                solved_problems.add(problem)
                final_score += time

                # Add penalties
                final_score += 20 * penalties[problem]
            elif solved:
                # Later right solutions of the problem
                pass
            else:
                # Not solved. Add as penalty
                penalties[problem] += 1

        n_solved_problems = len(solved_problems)
        self.put_string(str(n_solved_problems) + " " + str(final_score))


def main():
    """Main method."""

    CPSolver()()


if __name__ == "__main__":
    main()
