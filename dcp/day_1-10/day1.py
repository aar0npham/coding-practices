'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


def function(list, k):
    isK = False
    for i in list:
        inv = k - i
        if inv in list:
            isK = True
        else:
            isK = False
    return isK


# Driver code
list = [10, 15, 3, 7]
k = 17
print(function(list, k))
