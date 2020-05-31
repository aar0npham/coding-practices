'''
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:
    a
   / \
  b   c
 / \ / \
d  e f  g
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder and not inorder:
        return None

    root = Node(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:idx + 1], inorder[:idx])
    root.right = buildTree(preorder[idx + 1:], inorder[idx + 1:])
    return root


pre = ['a', ' b', ' d', ' e', ' c', 'f', 'g']
inor = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
print(buildTree(pre, inor))
