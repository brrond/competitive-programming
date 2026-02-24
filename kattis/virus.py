"""
Link: https://open.kattis.com/problems/virus
"""

import sys


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

        # This n is for testing purpose only
        # in reality n is always 1
        n = 1
        if self.debug:
            n = self.get_int()

        for _ in range(n):
            original = self.get_string().strip()
            modified = self.get_string().strip()

            # strip beginning
            i = j = 0
            while i < len(original) and j < len(modified):
                if original[i] != modified[j]:
                    break
                i += 1
                j += 1

            # modified string is just a substring of the original string
            # no insertion operations are made
            if j == len(modified):
                self.put_string(str(0))
                continue

            # At this point there are two cases:
            # both string have some elements
            # first (original) string has no more elements
            # it doesn't matter, which one we have

            # reverse strings, as the beginning was stripped
            rest_of_original = original[i:][::-1]
            rest_of_modified = modified[j:][::-1]

            # reversed index
            i = 0
            j = 0
            while i < len(rest_of_original) and j < len(rest_of_modified):
                if rest_of_original[i] != rest_of_modified[j]:
                    break
                i += 1
                j += 1

            # modified string is just a substring of the original string
            # with some elements deleted in the middle
            # no insertion operations are made
            if j == len(rest_of_modified):
                self.put_string("0")
                continue

            # At this point there are two cases:
            # both string have some elements
            # first (original) string has no more elements
            # it doesn't matter which case it is
            result = len(rest_of_modified) - j
            self.put_string(str(result))


def main():
    """Main method."""

    CPSolver(True)()


if __name__ == "__main__":
    main()
