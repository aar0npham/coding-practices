'''
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''
arr = [2, 4, 1, 3, 5]

def day44(arr):
    if len(arr) == 1:
        return arr

    p1 = arr[:len(arr) // 2]
    p2 = arr[len(arr) // 2:]

    p1, p1i = day44(p1)
    p2, p2i = day44(p2)
    c = []
    i, j = 0, 0

    inversion = 0 + p1i + p2i
    while i < len(p1) and j < len(p2):
        if p1[i] < p2[j]:
            c.append(p1[i])
            i += 1
        else:
            c.append(p2[j])
            j += 1
            inversion += len(p1) - i
    c += p1[i:]
    c += p2[:j]
    return c, inversion
