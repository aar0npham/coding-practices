'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons_func):
    def _car(a,b):
        return a
    return cons_func(_car)

def cdr(cons_func):
    def _cdr(a,b):
        return b
    return cons_func(_cdr)

car(cons(3, 4))
cdr(cons(3, 4))
