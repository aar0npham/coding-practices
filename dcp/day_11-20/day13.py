'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def find_substring(s, k):
    if not s:
        return ''
    elif len(s) <= k:
        return s
    elif k == 1:
        return s[0]

    distinct = 0
    seen = set()
    first_idx = 0
    second_idx = 0

    while s[second_idx] == s[first_idx]:
        second_idx += 1

    for idx, char in enumerate(s):
        if char not in seen:
            seen.add(char)
            distinct += 1

        if distinct > k:
            poss = s[:idx]
            remain = s[second_idx:]
            break

    max_remain = find_substring(remain, k)

    if len(poss) < len(max_remain):
        max_substring = max_remain
    else:
        max_substring = poss
    return max_substring


# Driver code
inp = "fafageradfj"
k = 4
print(find_substring(inp, k))
