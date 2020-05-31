'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def unival(node):
    return helper(node, node.value)


def helper(node, value):
    if not node:
        return True
    if node.value == value:
        return helper(node.left, value) and helper(node.right, value)
    return False

def count(node):
    if not node:
        return 0
    num = count(node.left) + count(node.right)
    if unival(node):
        num+=1
    return num

# Driver code
node1 = Node('0', Node('1'), Node('0', Node('1', Node('1'), Node('1')), Node('0')))
node2 = Node('0', Node('1'), Node('1'))
node3 = Node('0', Node('0', Node('0'), Node('0')), Node('0'))
node4 = Node('1')
print(count(node1))
