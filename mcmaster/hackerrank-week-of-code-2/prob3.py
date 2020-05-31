def remove(arr, query):
    # when query == 2
    return arr.pop()


def add(arr, query):
    # when query == 1
    return arr.append(query[1])


def calc(arr, query):
    sum = 0
    for i in range(query[1], query[2]+1):
        sum += arr[i]
    print(sum)


if __name__ == '__main__':
    n, m = input().split()
    arr = list(map(int, input().split()))
    ql = []
    for i in range(int(m)):
        ql.append(list(map(int, input().split())))
    for qu in ql:
        if qu[0] == 0:
            calc(arr, qu)
        elif qu[0] == 1:
            add(arr, qu)
        elif qu[0] == 2:
            remove(arr, qu)
