def lastOcc(arr, low, high, x, n):

    if low > high:
        return -1

    mid = (low + high) // 2

    if x > arr[mid]:
        return lastOcc(arr, mid + 1, high, x, n)

    elif x < arr[mid]:
        return lastOcc(arr, low, mid - 1, x, n)

    else:
        if mid == n - 1 or arr[mid + 1] != arr[mid]:
            return mid
        else:
            return lastOcc(arr, mid + 1, high, x, n)


if __name__ == "__main__":
    arr = [5, 10, 10, 10, 10, 20, 20]
    n = 7
    x = 10

    print(lastOcc(arr, 0, n - 1, x, n))
