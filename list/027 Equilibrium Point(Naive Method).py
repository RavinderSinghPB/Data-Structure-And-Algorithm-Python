def checkEquilibrium(arr, n):

    for i in range(0, n):

        l_sum = 0
        r_sum = 0

        for j in range(0, i):
            l_sum += arr[j]

        for j in range(i + 1, n):
            r_sum += arr[j]

        if l_sum == r_sum:
            return True

    return False


if __name__ == "__main__":
    arr = [3, 4, 8, -9, 20, 6]
    n = len(arr)

    print(checkEquilibrium(arr, n))
