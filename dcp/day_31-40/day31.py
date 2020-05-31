'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”,
and append a “g”.

Given two strings, compute the edit distance between them.
(Wagner-Fischer algorithm [Levenstein distance])
'''

s1 = 'kitten'
s2 = 'sitting'


def edit_distance(s1, s2):
    arr = [[0 for x in range(len(s1) + 1)] for y in range(len(s2) + 1)]

    for i in range(len(s1) + 1):
        arr[0][i] = i

    for j in range(len(s2) + 1):
        arr[j][0] = j

    for j in range(1, len(s2) + 1):
        for i in range(1, len(s1) + 1):
            a1 = arr[j][i - 1] + 1
            a2 = arr[j - 1][i] + 1
            a3 = arr[j - 1][i - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
            arr[j][i] = min(a1, a2, a3)

    return arr[-1][-1]


print(edit_distance(s1, s2))
