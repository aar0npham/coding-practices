'''
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport,
compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''
arr1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'
arr2 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'

def lex(arr, start):
    # keys to find corresponding values
    # sort() final and pick first one
    # remove el recursively
    result = [x for x in arr if x[0]==start]

    if len(result)==0:
        return None
    else:
        result.sort()
        el = result[0]
        n_arr = [x for x in arr if x!=el]
        it=[el[0]]

        if len(n_arr)==0:
            it.extend(el[1])
        else:
            it.extend(lex(n_arr, el[1]))

    return it

print(lex(arr1[0], arr1[1]))
print(lex(arr2[0],arr2[1]))
