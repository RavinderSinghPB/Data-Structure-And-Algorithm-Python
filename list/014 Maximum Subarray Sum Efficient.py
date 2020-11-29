def maxSum(arr, n):
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, n):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(maxEnding, res)

    return res


if __name__ == "__main__":
    arr = [1, -2, 3, -1, 2]
    n = len(arr)

    print(maxSum(arr, n))
