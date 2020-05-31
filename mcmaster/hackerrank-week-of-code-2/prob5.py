from math import ceil, floor


def check_palidrome(string):
    if len(string) % 2 == 0:
        i = int(len(string) / 2)
        return string[i:] == string[:i][::-1]
    else:
        i1 = int(floor(float(len(string)) / 2))
        i2 = int(ceil(float(len(string)) / 2))
        return string[i1:] == string[:i2][::-1]


def cut(string):
    i = 0
    f = len(string)
    if check_palidrome(string):
        print(i, f-f)
    else:
        while i < len(string):
            check_palidrome(string[i + 1, f - 1])
        print(i, f)


if __name__ == '__main__':
    n = input().split()
    string = input()
    cut(string)
