def cave(m, i_arr):
    c_arr = []
    for i in range(len(i_arr)):
        cl = int(m) - (i_arr[i])
        c_arr.append(cl)
    print(sorted(c_arr)[0])


if __name__ == '__main__':
    n, m = input().split()
    if int(n) == 0:
        print(int(m))
    else:
        arr = list(map(int, input().rstrip().split()))
        cave(m, arr)
