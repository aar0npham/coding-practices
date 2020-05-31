'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

adj1 =  [2, 4, 6, 2, 5] # 13
adj2 =  [5, 1, 1, 5] # 10
adj3 = [9, 1, 1, 9, 1, 9, 1, 9, 9, 8, 7, 8] # 52

def non_adjacent(nums):
    if len(nums) <= 2:
        return max(nums)
    else:
        excl = max(nums[0], 0)
        incl = max(nums[1], nums[1])

        for x in range(2, len(nums)):
            if excl > incl:
                new_e = excl
            else:
                new_e = incl

            incl = excl + nums[x]
            excl = new_e
        return max(excl, incl)



# Driver code
print(non_adjacent(adj1))
print(non_adjacent(adj2))
print(non_adjacent(adj3))
