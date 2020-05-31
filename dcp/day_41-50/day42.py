'''
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''
ex = [12, 1, 61, 5, 9, 2], 24

def list_sum(s, k):
    kf = k
    s = sorted([x for x in s if x <=k])
    out = []

    while sum(out)!=kf:
        if len(s) == 0:
            return None

        if s[-1]>k:
            s.pop()
        p = s.pop()
        k-=p
        out.append(p)

    return out

print(list_sum(ex[0], ex[1]))
