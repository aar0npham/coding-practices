'''
This problem was asked by Google.

The area of a circle is defined as pi*r^2. Estimate pi to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

import random


def est_pi():
    iter = 100000
    inside = 0

    for i in range(iter):
        x = random.random()**2
        y = random.random()**2
        if (x + y) < 1:
            inside += 1
    pi = float(inside) / float(iter) * 4
    return pi


print(est_pi())
