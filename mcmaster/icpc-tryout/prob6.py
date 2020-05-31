from itertools import groupby
from itertools import product


def neighbours(size, cell):
    for c in product(*(range(n - 1, n + 2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c


def count_infected(n, infect):
    count = 0
    neig_infec = []
    for l in infect:
        for i in list(neighbours(n, (l[0], l[1]))):
            neig_infec.append(i)
        neig_infec = sorted(neig_infec)
    final = list(neig_infec for neig_infec, _ in groupby(neig_infec))
    # print(final)
    count += len(final)
    return count


if __name__ == '__main__':
    inp = list(map(int, input().split()))
    infect = []
    for i in range(inp[0]):
        infect.append(list(map(int, input().split())))
    print(count_infected(inp[0], infect))
