'''
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the
list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2,1.5,2,3.5,2,2,2
'''

test = [2, 1, 5, 7, 2, 0, 5]

def median(arr):
    n = len(arr)
    if n%2==1:
        return arr[n//2]
    else:
        return sum(arr[n//2-1:n//2+1])/2.0

def running_median(arr):
    s = []
    for x in arr:
        s.append(x)
        s = sorted(s)
        print(median(s))

running_median(test)
