'''
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

arr1 = [34, -50, 42, 14, -5, 86]
arr2 = [-5, -1, -8, -9]


def day49(arr):
    current = arr[0]
    concurrent = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        concurrent = max(concurrent, current)

    return max(concurrent, 0)


print(day49(arr1))
print(day49(arr2))
