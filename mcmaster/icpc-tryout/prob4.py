from itertools import chain, combinations

tab = 1
ret = 2
spc = 3
conf = 6

ws=[1,2,3]

def count(n):
    if n < 6:
        return 0
    count = 0
    list = ['-']*n
