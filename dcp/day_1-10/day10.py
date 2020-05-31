'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import time

def f():
    return 1

def scheduler(function, n):
    time.sleep(n/1000.)
    return function

print(scheduler(f(), 5))
