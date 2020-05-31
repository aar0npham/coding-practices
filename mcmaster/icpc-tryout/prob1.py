def prob1(arr):
    for i in arr:
        if i==8:
            arr.remove(arr[arr.index(i)+1])
            arr.remove(i)
    return arr

arr = [6,7,8,9]
print(prob1(arr))
