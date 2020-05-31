'''
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''
from collections import defaultdict
import random
import math


def rand5():
    return math.floor(random.uniform(1, 5))


def day45():
    while True:
        n = 5 * (rand5() - 1) + (rand5() - 1)
        if n < 21:
            return n % 7 + 1


results = defaultdict(int)

for i in range(100000):
    results[day45()] += 1

for x in results.keys():
    print(x, results[x] / 1000.)
