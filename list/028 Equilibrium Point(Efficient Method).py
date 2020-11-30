def checkEquilibrium(arr, n):
    sm = 0

    for i in range(0, n):
        sm += arr[i]

    l_sum = 0

    for i in range(0, n):

        if l_sum == sm - arr[i]:
            return True
        l_sum += arr[i]
        sm -= arr[i]

    return False


if __name__ == "__main__":
    arr = [3, 4, 8, -9, 20, 6]
    n = len(arr)

    print(checkEquilibrium(arr, n))
