'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
'''

test = [[5, 2, 1],
        [3, 1, 1],
        [10, 9, 3]]

def mincost(arr):
    p_idx = arr[0].index(min(arr[0]))
    cost = arr[0][p_idx]
    for n in arr[1:]:
        n.pop(p_idx)
        cost += min(n)
        p_idx = n.index(min(n))

    return cost

print(mincost(test))
