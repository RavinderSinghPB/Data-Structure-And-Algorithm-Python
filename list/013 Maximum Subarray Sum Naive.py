def maxSum(arr, n):
    res = arr[0]

    for i in range(0, n):
        curr = 0

        for j in range(i, n):
            curr = curr + arr[j]
            res = max(res, curr)

    return res


if __name__ == "__main__":
    arr = [1, -2, 3, -1, 2]
    n = len(arr)

    print(maxSum(arr, n))
