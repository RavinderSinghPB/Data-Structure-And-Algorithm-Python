def firstOccurrence(arr, low, high, x):
    if low > high:
        return -1

    mid = (low + high) // 2

    if x > arr[mid]:
        return firstOccurrence(arr, mid + 1, high, x)
    elif x < arr[mid]:
        firstOccurrence(arr, low, mid - 1, x)
    else:

        if mid == 0 or arr[mid - 1] != arr[mid]:
            return mid
        else:
            return firstOccurrence(arr, low, mid - 1, x)


if __name__ == "__main__":
    arr = [5, 10, 10, 15, 20, 20, 20]
    n = 7
    x = 20

    print(firstOccurrence(arr, 0, n - 1, x))
