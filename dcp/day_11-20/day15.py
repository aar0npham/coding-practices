'''
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
Reservoir Sampling
'''
import random

def pick(bigstream):
    random_element = None

    for i, e in enumerate(bigstream):
        if i ==0:
            random_element=e
        elif random.randint(1, i+1)==1:
            random_element=e
        return random_element
