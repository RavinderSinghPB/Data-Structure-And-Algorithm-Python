def normalMaxSum(arr, n):
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, n):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(maxEnding, res)

    return res


def overallMaxSum(arr, n):
    max_normal = normalMaxSum(arr, n)

    if max_normal < 0:
        return max_normal

    arr_sum = 0

    for i in range(0, n):
        arr_sum += arr[i]
        arr[i] = -arr[i]

    max_circular = arr_sum + normalMaxSum(arr, n)
    return max(max_circular, max_normal)


if __name__ == "__main__":
    arr = [8, -4, 3, -5, 4]
    n = len(arr)

    print(overallMaxSum(arr, n))
