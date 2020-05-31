'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''
d1 = set(['quick', 'brown', 'the', 'fox'])
s1 = "thequickbrownfox"
d2 = set(['bed', 'bath', 'bedbath', 'and', 'beyond'])
s2 = "bedbathandbeyond"


def finddict(dict, string):
    pt0 = 0
    pt1 = 1
    res = []
    while pt1 < len(string) + 1:
        if string[pt0:pt1] in dict:
            res.append(string[pt0:pt1])
            pt0 = pt1
        pt1 += 1
    return res


print(finddict(d1, s1))
print(finddict(d2, s2))
