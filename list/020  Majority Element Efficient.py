def findMajority(arr, n):
    res = 0
    count = 1

    for i in range(1, n):

        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            res = i
            count = 1

    count = 0

    for i in range(0, n):
        if arr[res] == arr[i]:
            count += 1

    if count <= n // 2:
        res = -1

    return res


if __name__ == "__main__":
    arr = [8, 7, 6, 8, 6, 6, 6, 6]
    n = len(arr)

    idx = findMajority(arr, n)
    if idx != -1:
        print(arr[idx])
