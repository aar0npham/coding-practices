'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

arr = [(30, 75), (0, 50), (60, 150)]
max(max(arr))*[0]

def findroom(arr):
    times = [0]*max(max(arr))
    for pair in arr:
        times[pair[0]:pair[1]]=[x+1 for x in times[pair[0]:pair[1]]]
    return max(times)

print(findroom(arr))
