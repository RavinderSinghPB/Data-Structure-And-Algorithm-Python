def printFreq(arr, n):
    freq = 1
    i = 1

    while i < n:

        while i < n and arr[i] == arr[i - 1]:
            freq += 1
            i += 1

        print(arr[i - 1], ' ', freq)
        i += 1
        freq = 1


if __name__ == "__main__":
    arr = [10, 10, 20, 30, 30, 30]

    n = len(arr)

    printFreq(arr, n)
