'''
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''
arr = [13, 18, 25, 2, 8, 10]
element = 8

def day58(arr, element):
    bin_idx = findmin_binary(arr, 0, len(arr)-1)
    comb = arr[bin_idx:] + arr[:bin_idx]
    return binary_search(comb, 0, len(comb)-1, element) + bin_idx

def findmin_binary(arr, bot, top):
    mid = int((bot + top) / 2)
    if arr[mid] < arr[bot] and arr[mid] < arr[top]:
        return mid
    if arr[mid] > arr[bot] and arr[mid] > arr[top]:
        return mid + 1

    if arr[bot] > arr[mid]:
        v = findmin_binary(arr, bot, mid)
    return v


def binary_search(arr, low, high, val):
    if high < low:
        return None

    mid = int((low + high) / 2)
    if arr[mid] == val:
        return mid
    if arr[mid] < val:
        return binary_search(arr, mid, high, val)
    if arr[mid] > val:
        return binary_search(arr, low, mid, val)

print(day58(arr,element))
