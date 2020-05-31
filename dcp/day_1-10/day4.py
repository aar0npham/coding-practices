'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

inp = [3, 4, -1, 1]
# inp = [1, 2, 0]


def function(input):
    m = max(input)
    z_arr = ['-'] * m
    for i in input:
        if i > 0:
            z_arr[i - 1] = 'x'

    # print(z_arr)
    try:
        return z_arr.index('-') + 1
    except:
        return m + 1

print(function(inp))
