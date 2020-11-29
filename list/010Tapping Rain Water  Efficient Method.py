def getWater(arr, n):

    res = 0
    lMax = [0] * n
    rMax = [0] * n

    lMax[0] = arr[0]

    for i in range(1, n):
        lMax[i] = max(arr[i], lMax[i - 1])

    rMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rMax[i] = max(arr[i], rMax[i + 1])

    for i in range(1, n - 1):
        res = res + (min(lMax[i], rMax[i]) - arr[i])

    return res


if __name__ == "__main__":
    arr = [3, 0, 1, 2, 5]
    n = len(arr)

    print(getWater(arr, n))
