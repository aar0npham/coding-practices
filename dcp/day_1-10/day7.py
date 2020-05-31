'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def decode(inp):
    count = 0
    def checkones(inp, count = 0):
        if int(inp[0]) in range(1,27):
            if len(inp) ==1:
                count +=1
            else:
                if len(inp) > 1:
                    inp = inp[1:]
                    count += checkones(inp)
                    if len(inp) > 2:
                        count += checktwos(inp)
        return count

    def checktwos(inp, count = 0):
        if int(inp[0:2]) in range(1,27):
            if len(inp) ==2:
                count +=1
            else:
                if len(inp) > 2:
                    inp = inp[2:]
                    count += checkones(inp)
                    if len(inp)>2:
                        count+= checktwos(inp)
        return count

    count += checkones(inp, count)
    count += checktwos(inp, count)
    return count

print(decode('1111'))
