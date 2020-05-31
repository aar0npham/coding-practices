'''
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
'''
s = 'the quick brown fox jumps over the lazy dog'

def day57(s, k):
    w = s.split(' ')
    result = []
    c = 0
    s = ''
    for i in range(len(w)):
        if c + len(w[i]) + 1 <=k:
            s += w[i]+' '
            c += len(w[i])
        else:
            result.append(s[:-1])
            c = len(w[i])
            s = w[i]+ ' '
    result.append(s[:-1])
    return result

print(day57(s, 10))
