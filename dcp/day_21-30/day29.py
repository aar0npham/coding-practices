'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
'''
test1 = 'AAAABBBCCDAA'
test2 = '4A3B2C1D2A'


def encode(string):
    out = ''
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
            if i == len(string) - 1:
                out += str(count)
                out += string[i - 1]
                count = 1
        else:
            out += str(count)
            out += string[i - 1]
            count = 1
    return out


def isnum(s):
    try:
        int(x=s)
        return True
    except:
        return False


def decode(string):
    out = ''
    p1 = 0
    p2 = 1

    while p2 < len(string) - 1:
        if isnum(string[p1:p2]):
            p2 += 1
        else:
            n = p2 - p1
            out += string[p1] * n
            p1 = p2
            p2 += 1
    return out


print(encode(test1))
print(decode(test2))
