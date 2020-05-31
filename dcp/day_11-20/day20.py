'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class Node:
    def __init__(self, val = None, nextval= None):
        self.val = val
        self.nextval = nextval

def lenLinked(A):
    curNode = A
    count = 1
    while curNode.nextval is not None:
        curNode = curNode.nextval
        count+=1
    return count

def intersection(A,B):
    lA,lB = lenLinked(A), lenLinked(B)

    if lA > lB:
        large, small = lA, lB
    else:
        large, small = lA, lB

    diff = abs(lA-lB)

    for i in range(diff):
        a = A.nextval

    while A.nextval is not None:
        if A.nextval.val == B.nextval.val:
            return A.nextval.val
        A = A.nextval
        B = B.nextval
    return 0


A = Node(3, Node(7, Node(8, Node(10))))
B = Node(99, Node(1, Node(8, Node(10))))
print(intersection(A,B))
