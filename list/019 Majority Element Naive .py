def findMajority(arr, n):
    for i in range(0, n):
        count = 1

        for j in range(i + 1, n):

            if arr[i] == arr[j]:
                count += 1

        if count > n / 2:
            return i
    return -1


if __name__ == "__main__":
    arr = [8, 7, 6, 8, 6, 6, 6, 6]
    n = len(arr)

    idx = findMajority(arr, n)
    if idx != -1:
        print(arr[idx])
