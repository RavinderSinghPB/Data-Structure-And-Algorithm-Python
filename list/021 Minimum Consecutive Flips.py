def printGroups(arr, n):

    for i in range(1, n):

        if arr[i] != arr[i - 1]:

            if arr[i] != arr[0]:
                print('from ', i, 'to', end=' ')
            else:
                print(i - 1)

    if arr[n - 1] != arr[0]:
        print(n - 1)


if __name__ == "__main__":
    arr = [0, 0, 1, 1, 0, 0, 1, 1, 0]
    n = len(arr)

    printGroups(arr, n)
