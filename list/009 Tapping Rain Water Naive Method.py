def getWater(arr, n):

    res = 0
    for i in range(1, n - 1):

        lMax = arr[i]

        for j in range(0, i):
            lMax = max(lMax, arr[j])

        rMax = arr[i]

        for j in range(i + 1, n):
            rMax = max(rMax, arr[j])

        res = res + (min(lMax, rMax) - arr[i])

    return res


if __name__ == "__main__":
    arr = [3, 0, 1, 2, 5]
    n = len(arr)

    print(getWater(arr, n))
