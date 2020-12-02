def firstOccurrence(arr, n, x):
    low = 0
    high = n - 1

    while low <= high:

        mid = (low + high) // 2

        if x > arr[mid]:
            low = mid + 1

        elif x < arr[mid]:
            high = mid - 1

        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid

            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [5, 10, 10, 10, 20]
    n = 5
    x = 10

    print(firstOccurrence(arr, n, x))
