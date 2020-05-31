from itertools import product


# assume that in every test case land is l



if __name__ == '__main__':
    n,m,c=input().split()
    matrix = []
    for i in range(int(n)):
        entries = list(map(str, input().split()))
        matrix.append(entries)
