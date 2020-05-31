'''
This problem was recently asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def function(list, n):
    i, temp = 1, 1
    prod = [1 for i in range(n)]

    for i in range(n):
        prod[i] = temp
        temp *= list[i]

    temp = 1

    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= list[i]

    for i in range(n):
        print(prod[i], end=' ')

    return


# Driver code
arr = [1, 2, 3, 4, 5]
function(arr, len(arr))
