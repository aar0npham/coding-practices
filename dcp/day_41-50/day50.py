'''

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluate(root):
    if root == '+':
        return evaluate(root.left)+evaluate(root.right)
    elif root == '-':
        return evaluate(root.left)-evaluate(root.right)
    elif root == '*':
        return evaluate(root.left)*evaluate(root.right)
    elif root == '/':
        return evaluate(root.left)/evaluate(root.right)
    else:
        return root.val
