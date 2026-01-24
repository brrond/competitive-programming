"""
Link:

Geir is not particularly good with computers, so when it comes to opening files he often
has trouble.
This often delays his teaching as he sometimes has to open files in class
to show his students something.
To get things running more smoothly his friend prepared a list of file extensions
(nafnauki in Icelandic) and what he should do for each of them.
For example it said that for MP4 files he could double click on it to open a video player,
double click to put it into full screen,
click once more to start the playback and then finally move his cursor off the player.

This was all well and good, but when it came to using this list Geir realised he had no idea
how to tell what the extension of a given file is. Can you help him?

File extensions will always be one to five letters long.
They are defined as whatever follows the last dot in the name of the file.
Input

The input is a single line, the name of the file Geir is trying to open.
The file name will contain only the ASCII letters a to z,
lower or upper case, along with dots and the digits
to . The file name will always have a valid file extension as noted above. The file name is at most

letters.
Output

Print the file extension of the file, with the dot.
Scoring

Group


Points


Constraints

1


30


The file extension is exactly

letters.

2


40


There is exactly one dot in the file name.

3


30


No further constraints.
Sample Input 1 	Sample Output 1

myndband.mp4



.mp4

Sample Input 2 	Sample Output 2

model.blend



.blend

Sample Input 3 	Sample Output 3

data.tar.gz


.gz
"""

inp = input()
index_of_dot = inp.rfind(".")
print(inp[index_of_dot:])
