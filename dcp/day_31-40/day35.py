'''
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''
arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']


def swap(l, p1, p2):
    l[p1], l[p2] = l[p2], l[p1]


def replace_rgb(arr):
    R_r = 0
    for R_n in range(len(arr)):
        if arr[R_n] == 'R':
            swap(arr, R_n, R_r)
            R_r += 1
    G_r = 0
    for G_n in range(len(arr)):
        if arr[G_n] == 'G':
            swap(arr, G_n, G_r + R_r)
            G_r += 1

    return arr


print(replace_rgb(arr))
