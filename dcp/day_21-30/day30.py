'''
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is
unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

test1 = [2, 1, 2]
test2 = [3, 0, 1, 3, 0, 5]


def sumwater(arr):
    left = 0
    right = len(arr) - 1
    max_left = 0
    max_right = 0
    water = 0

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] > max_left:
                max_left = arr[left]
            else:
                water += max_left - arr[left]
            left += 1
        else:
            if arr[right] > max_right:
                max_right = arr[right]
            else:
                water += max_right - arr[right]
            right -= 1

    return water

print(sumwater(test1))
print(sumwater(test2))
