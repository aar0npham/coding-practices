def count_fish(f, val, r):
    valid = False
    for dir in r:
        if val >= dir[0] and val <= dir[1]:
            valid = True
    return valid


if __name__ == '__main__':
    n, f, l = input().split()
    count = 0
    i = 0
    dir = []
    while i < int(n):
        dir.append(list(map(int, input().split())))
        i+=1
    for i in range(int(f)):
        val = input()
        isValid = count_fish(int(f), int(val), dir)
        if isValid is True:
            count += 1
    print(count)
