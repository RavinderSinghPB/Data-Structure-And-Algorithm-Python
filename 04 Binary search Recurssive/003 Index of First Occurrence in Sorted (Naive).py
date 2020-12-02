def firstOccurrence(arr, n, x):
    for i in range(0, n):

        if arr[i] == x:
            return i

    return -1


if __name__ == "__main__":
    arr = [5, 10, 10, 15, 15]
    n = 5
    x = 15

    print(firstOccurrence(arr, n, x))
